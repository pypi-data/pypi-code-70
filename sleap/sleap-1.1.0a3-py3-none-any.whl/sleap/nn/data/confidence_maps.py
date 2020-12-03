"""Transformers for confidence map generation."""

import tensorflow as tf
import attr
from typing import List, Text
from sleap.nn.data.utils import make_grid_vectors


def make_confmaps(
    points: tf.Tensor, xv: tf.Tensor, yv: tf.Tensor, sigma: float
) -> tf.Tensor:
    """Make confidence maps from a set of points from a single instance.

    Args:
        points: A tensor of points of shape (n_nodes, 2) and dtype tf.float32 where the
            last axis corresponds to (x, y) pixel coordinates on the image. These can
            contain NaNs to indicate missing points.
        xv: Sampling grid vector for x-coordinates of shape (grid_width,) and dtype
            tf.float32. This can be generated by
            `sleap.nn.data.utils.make_grid_vectors`.
        yv: Sampling grid vector for y-coordinates of shape (grid_height,) and dtype
            tf.float32. This can be generated by
            `sleap.nn.data.utils.make_grid_vectors`.
        sigma: Standard deviation of the 2D Gaussian distribution sampled to generate
            confidence maps.

    Returns:
        Confidence maps as a tensor of shape (grid_height, grid_width, n_nodes) of dtype
        tf.float32.

        Each channel of the confidence maps will contain the unnormalized PDF of a 2D
        Gaussian distribution with a mean centered at the coordinates of the
        corresponding point, and diagonal covariance matrix (i.e., the same standard
        deviation for both dimensions).

        When the point is perfectly aligned to the sampling grid, the value at that grid
        coordinate is 1.0 since the PDF is not normalized.

        If a point was missing (indicated by NaNs), the corresponding channel will
        contain all zeros.

    See also: sleap.nn.data.make_grid_vectors, make_multi_confmaps
    """
    x = tf.reshape(tf.gather(points, [0], axis=1), [1, 1, -1])
    y = tf.reshape(tf.gather(points, [1], axis=1), [1, 1, -1])
    cm = tf.exp(
        -((tf.reshape(xv, [1, -1, 1]) - x) ** 2 + (tf.reshape(yv, [-1, 1, 1]) - y) ** 2)
        / (2 * sigma ** 2)
    )
    cm = tf.math.maximum(0.0, cm)  # Replaces NaNs with 0.
    return cm


def make_multi_confmaps(
    instances: tf.Tensor, xv: tf.Tensor, yv: tf.Tensor, sigma: float
) -> tf.Tensor:
    """Make confidence maps for multiple instances through max reduction.

    Args:
        instances: A tensor of shape (n_instances, n_nodes, 2) and dtype tf.float32
            containing instance points where the last axis corresponds to (x, y) pixel
            coordinates on the image. This must be rank-3 even if a single instance is
            present.
        xv: Sampling grid vector for x-coordinates of shape (grid_width,) and dtype
            tf.float32. This can be generated by
            `sleap.nn.data.utils.make_grid_vectors`.
        yv: Sampling grid vector for y-coordinates of shape (grid_height,) and dtype
            tf.float32. This can be generated by
            `sleap.nn.data.utils.make_grid_vectors`.
        sigma: Standard deviation of the 2D Gaussian distribution sampled to generate
            confidence maps.

    Returns:
        Confidence maps as a tensor of shape (grid_height, grid_width, n_nodes) of dtype
        tf.float32.

        Each channel will contain the elementwise maximum of the confidence maps
        generated from all individual points for the associated node.

    Notes:
        The confidence maps are for each instance are computed individually and
        immediately max-reduced to avoid maintaining the entire set of all instance
        confidence maps. This enables memory-efficient generation of multi-instance
        confidence maps for examples with large numbers of instances.

    See also: sleap.nn.data.make_grid_vectors, make_confmaps
    """
    grid_height = tf.shape(yv)[0]
    grid_width = tf.shape(xv)[0]
    n_nodes = tf.shape(instances)[1]
    cms = tf.zeros((grid_height, grid_width, n_nodes), tf.float32)

    in_img = (instances > 0) & (
        instances < tf.reshape(tf.stack([xv[-1], yv[-1]], axis=0), [1, 1, 2])
    )
    in_img = tf.reduce_any(tf.reduce_all(in_img, axis=-1), axis=1)
    in_img = tf.ensure_shape(in_img, [None])
    instances = tf.boolean_mask(instances, in_img)

    for points in instances:
        cms = tf.maximum(cms, make_confmaps(points, xv=xv, yv=yv, sigma=sigma))
    return cms


@attr.s(auto_attribs=True)
class MultiConfidenceMapGenerator:
    """Transformer to generate multi-instance confidence maps.

    Attributes:
        sigma: Standard deviation of the 2D Gaussian distribution sampled to generate
            confidence maps. This defines the spread in units of the input image's grid,
            i.e., it does not take scaling in previous steps into account.
        output_stride: Relative stride of the generated confidence maps. This is
            effectively the reciprocal of the output scale, i.e., increase this to
            generate confidence maps that are smaller than the input images.
        centroids: If True, generate confidence maps for centroids rather than instance
            points.
    """

    sigma: float = 1.0
    output_stride: int = 1
    centroids: bool = False

    @property
    def input_keys(self) -> List[Text]:
        """Return the keys that incoming elements are expected to have."""
        if self.centroids:
            return ["image", "centroids"]
        else:
            return ["image", "instances"]

    @property
    def output_keys(self) -> List[Text]:
        """Return the keys that outgoing elements will have."""
        if self.centroids:
            return self.input_keys + ["centroid_confidence_maps"]
        else:
            return self.input_keys + ["confidence_maps"]

    def transform_dataset(self, input_ds: tf.data.Dataset) -> tf.data.Dataset:
        """Create a dataset that contains the generated confidence maps.

        Args:
            input_ds: A dataset with elements that contain the keys "image", "scale" and
                either "instances" or "centroids" depending on whether the `centroids`
                attribute is set to True.

        Returns:
            A `tf.data.Dataset` with the same keys as the input, as well as a
            "confidence_maps" or "centroid_confidence_maps" key containing the generated
            confidence maps.

        Notes:
            The output stride is relative to the current scale of the image. To map
            points on the confidence maps to the raw image, first multiply them by the
            output stride, and then scale the x- and y-coordinates by the "scale" key.

            Importantly, the sigma will be proportional to the current image grid, not
            the original grid prior to scaling operations.
        """
        # Infer image dimensions to generate the full scale sampling grid.
        test_example = next(iter(input_ds))
        image_height = test_example["image"].shape[0]
        image_width = test_example["image"].shape[1]

        # Generate sampling grid vectors.
        xv, yv = make_grid_vectors(
            image_height=image_height,
            image_width=image_width,
            output_stride=self.output_stride,
        )

        def generate_multi_confmaps(example):
            """Local processing function for dataset mapping."""
            if self.centroids:
                example["centroid_confidence_maps"] = make_multi_confmaps(
                    tf.expand_dims(example["centroids"], axis=1),
                    xv=xv,
                    yv=yv,
                    sigma=self.sigma * self.output_stride,
                )
            else:
                example["confidence_maps"] = make_multi_confmaps(
                    example["instances"],
                    xv=xv,
                    yv=yv,
                    sigma=self.sigma * self.output_stride,
                )
            return example

        # Map transformation.
        output_ds = input_ds.map(
            generate_multi_confmaps, num_parallel_calls=tf.data.experimental.AUTOTUNE
        )
        return output_ds


@attr.s(auto_attribs=True)
class InstanceConfidenceMapGenerator:
    """Transformer to generate instance-centered confidence maps.

    Attributes:
        sigma: Standard deviation of the 2D Gaussian distribution sampled to generate
            confidence maps. This defines the spread in units of the input image's grid,
            i.e., it does not take scaling in previous steps into account.
        output_stride: Relative stride of the generated confidence maps. This is
            effectively the reciprocal of the output scale, i.e., increase this to
            generate confidence maps that are smaller than the input images.
        all_instances: If True, will also generate the multi-instance confidence maps.
    """

    sigma: float = 1.0
    output_stride: int = 1
    all_instances: bool = False

    @property
    def input_keys(self) -> List[Text]:
        """Return the keys that incoming elements are expected to have."""
        if self.all_instances:
            return ["instance_image", "center_instance", "all_instances"]
        else:
            return ["instance_image", "center_instance"]

    @property
    def output_keys(self) -> List[Text]:
        """Return the keys that outgoing elements will have."""
        if self.all_instances:
            return self.input_keys + [
                "instance_confidence_maps",
                "all_instance_confidence_maps",
            ]
        else:
            return self.input_keys + ["instance_confidence_maps"]

    def transform_dataset(self, input_ds: tf.data.Dataset) -> tf.data.Dataset:
        """Create a dataset that contains the generated confidence maps.

        Args:
            input_ds: A dataset with elements that contain the keys "instance_image",
                "center_instance" and, if the attribute `all_instances` is True,
                "all_instances".

        Returns:
            A `tf.data.Dataset` with the same keys as the input, as well as
            "instance_confidence_maps" and, if the attribute `all_instances` is True,
            "all_instance_confidence_maps" keys containing the generated confidence
            maps.

        Notes:
            The output stride is relative to the current scale of the image. To map
            points on the confidence maps to the raw image, first multiply them by the
            output stride, and then scale the x- and y-coordinates by the "scale" key.

            Importantly, the sigma will be proportional to the current image grid, not
            the original grid prior to scaling operations.
        """
        # Infer image dimensions to generate sampling grid.
        test_example = next(iter(input_ds))
        image_height = test_example["instance_image"].shape[0]
        image_width = test_example["instance_image"].shape[1]

        # Generate sampling grid vectors.
        xv, yv = make_grid_vectors(
            image_height=image_height,
            image_width=image_width,
            output_stride=self.output_stride,
        )

        def generate_confmaps(example):
            """Local processing function for dataset mapping."""
            example["instance_confidence_maps"] = make_confmaps(
                example["center_instance"],
                xv=xv,
                yv=yv,
                sigma=self.sigma * self.output_stride,
            )

            if self.all_instances:
                example["all_instance_confidence_maps"] = make_multi_confmaps(
                    example["all_instances"],
                    xv=xv,
                    yv=yv,
                    sigma=self.sigma * self.output_stride,
                )

            return example

        # Map transformation.
        output_ds = input_ds.map(
            generate_confmaps, num_parallel_calls=tf.data.experimental.AUTOTUNE
        )
        return output_ds


@attr.s(auto_attribs=True)
class SingleInstanceConfidenceMapGenerator:
    """Transformer to generate single-instance confidence maps.

    Attributes:
        sigma: Standard deviation of the 2D Gaussian distribution sampled to generate
            confidence maps. This defines the spread in units of the input image's grid,
            i.e., it does not take scaling in previous steps into account.
        output_stride: Relative stride of the generated confidence maps. This is
            effectively the reciprocal of the output scale, i.e., increase this to
            generate confidence maps that are smaller than the input images.
    """

    sigma: float = 1.0
    output_stride: int = 1

    @property
    def input_keys(self) -> List[Text]:
        """Return the keys that incoming elements are expected to have."""
        return ["image", "instances"]

    @property
    def output_keys(self) -> List[Text]:
        """Return the keys that outgoing elements will have."""
        return self.input_keys + ["points", "confidence_maps"]

    def transform_dataset(self, input_ds: tf.data.Dataset) -> tf.data.Dataset:
        """Create a dataset that contains the generated confidence maps.

        Args:
            input_ds: A dataset with elements that contain the keys "instances" and
            "image".

        Returns:
            A `tf.data.Dataset` with the same keys as the input, as well as
            "confidence_maps" containing the generated confidence maps.

        Notes:
            The output stride is relative to the current scale of the image. To map
            points on the confidence maps to the raw image, first multiply them by the
            output stride, and then scale the x- and y-coordinates by the "scale" key.

            Importantly, the sigma will be proportional to the current image grid, not
            the original grid prior to scaling operations.
        """
        # Infer image dimensions to generate sampling grid.
        test_example = next(iter(input_ds))
        image_height = test_example["image"].shape[0]
        image_width = test_example["image"].shape[1]

        # Generate sampling grid vectors.
        xv, yv = make_grid_vectors(
            image_height=image_height,
            image_width=image_width,
            output_stride=self.output_stride,
        )

        def generate_confmaps(example):
            """Local processing function for dataset mapping."""
            # Pull out first instance as (n_nodes, 2) tensor.
            example["points"] = tf.gather(example["instances"], 0, axis=0)

            # Generate confidence maps.
            example["confidence_maps"] = make_confmaps(
                example["points"], xv=xv, yv=yv, sigma=self.sigma * self.output_stride
            )

            return example

        # Map transformation.
        output_ds = input_ds.map(
            generate_confmaps, num_parallel_calls=tf.data.experimental.AUTOTUNE
        )
        return output_ds

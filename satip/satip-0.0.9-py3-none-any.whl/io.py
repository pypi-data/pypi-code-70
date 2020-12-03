# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/03_zarr.ipynb (unless otherwise specified).

__all__ = ['is_retriable', 'load_from_zarr_bucket', 'add_constant_coord_to_da', 'Compressor', 'save_da_to_zarr']

# Cell
import pandas as pd
import xarray as xr
import numpy as np
import dask
import zarr
import gcsfs
import numcodecs

# Cell
def is_retriable(exception):
    """Returns True if this exception is retriable."""
    errors = list(range(500, 505)) + [
        400, # Jack's addition.  Google Cloud occasionally throws Bad Requests for no apparent reason.
        408,# Request Timeout
        429, # Too Many Requests
    ]

    errors += [str(e) for e in errors]

    if isinstance(exception, gcsfs.utils.HttpError):
        return exception.code in errors

    return isinstance(exception, gcsfs.utils.RETRIABLE_EXCEPTIONS)

gcsfs.utils.is_retriable = is_retriable

def load_from_zarr_bucket(zarr_bucket):
    gcs = gcsfs.GCSFileSystem()
    store = gcsfs.GCSMap(root=zarr_bucket, gcs=gcs)
    ds = xr.open_zarr(store, consolidated=True)

    return ds

# Cell
def add_constant_coord_to_da(da, coord_name, coord_val):
    """
    Adds a new coordinate with a
    constant value to the DataArray

    Parameters
    ----------
    da : xr.DataArray
        DataArrray which will have the new coords added to it
    coord_name : str
        Name for the new coordinate dimensions
    coord_val
        Value that will be assigned to the new coordinates

    Returns
    -------
    da : xr.DataArray
        DataArrray with the new coords added to it

    """

    da = (da
          .assign_coords({coord_name:coord_val})
          .expand_dims(coord_name)
         )

    return da

class Compressor:
    def __init__(self,
                 bits_per_pixel=10,
                 mins=np.array([-1.2278595, -2.5118103, -64.83977, 63.404694, 2.844452, 199.10002, -17.254883, -26.29155, -1.1009827, -2.4184198, 199.57048, 198.95093]),
                 maxs=np.array([103.90016, 69.60857, 339.15588, 340.26526, 317.86752, 313.2767, 315.99194, 274.82297, 93.786545, 101.34922, 249.91806, 286.96323]),
                 variable_order=['HRV', 'IR_016', 'IR_039', 'IR_087', 'IR_097', 'IR_108', 'IR_120', 'IR_134', 'VIS006', 'VIS008', 'WV_062', 'WV_073']
                ):

        locals_ = locals()
        attrs_to_add = ['bits_per_pixel', 'mins', 'maxs', 'variable_order']

        for attr in attrs_to_add:
            setattr(self, attr, locals_[attr])

        return

    def fit(self, da, dims=['time', 'y', 'x']):
        self.mins = da.min(dims).compute()
        self.maxs = da.max(dims).compute()
        self.variable_order = da.coords['variable'].values

        print(f'The mins are: {self.mins}')
        print(f'The maxs are: {self.maxs}')
        print(f'The variable order is: {self.variable_order}')

        return

    def compress(self, da):
        da_meta = da.attrs

        for attr in ['mins', 'maxs']:
            assert getattr(self, attr) is not None, f'{attr} must be set in initialisation or through `fit`'

        if 'time' not in da.dims:
            time = pd.to_datetime(da_meta['end_time'])
            da = add_constant_coord_to_da(da, 'time', time)

        da = (da
              .reindex({'variable': self.variable_order})
              .transpose('time', 'y', 'x', 'variable')
             )

        upper_bound = (2 ** self.bits_per_pixel) - 1
        new_max = self.maxs - self.mins

        da -= self.mins
        da /= new_max
        da *= upper_bound

        da = (da
              .fillna(-1)
              .round()
              .astype(np.int16)
             )

        da.attrs = {'meta': str(da_meta)} # Must be serialisable

        return da

# Cell
def save_da_to_zarr(da, zarr_bucket, dim_order=['time', 'x', 'y', 'variable'], zarr_mode='a'):
    da = da.transpose(*dim_order)
    _, y_size, x_size, _ = da.shape
    out_store = gcsfs.GCSMap(root=zarr_bucket, gcs=gcsfs.GCSFileSystem())

    chunks = (36, y_size, x_size, 1)

    ds = xr.Dataset({'stacked_eumetsat_data': da.chunk(chunks)})

    zarr_mode_to_extra_kwargs = {
        'a': {
            'append_dim': 'time'
        },
        'w': {
            'encoding': {
                'stacked_eumetsat_data': {
                    'compressor': numcodecs.Blosc(cname='zstd', clevel=5),
                    'chunks': chunks
                }
            }
        }
    }

    assert zarr_mode in ['a', 'w'], '`zarr_mode` must be one of: `a`, `w`'
    extra_kwargs = zarr_mode_to_extra_kwargs[zarr_mode]

    ds.to_zarr(out_store, mode=zarr_mode, consolidated=True, **extra_kwargs)

    return
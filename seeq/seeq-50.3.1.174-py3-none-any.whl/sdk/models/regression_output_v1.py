# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 50.3.1-BETA
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RegressionOutputV1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'adjusted_r_squared': 'float',
        'error_sum_squares': 'float',
        'intercept': 'float',
        'intercept_standard_error': 'float',
        'is_uncertain': 'bool',
        'regression_sum_squares': 'float',
        'rsquared': 'float',
        'suggested_p_value_cutoff': 'float'
    }

    attribute_map = {
        'adjusted_r_squared': 'adjustedRSquared',
        'error_sum_squares': 'errorSumSquares',
        'intercept': 'intercept',
        'intercept_standard_error': 'interceptStandardError',
        'is_uncertain': 'isUncertain',
        'regression_sum_squares': 'regressionSumSquares',
        'rsquared': 'rsquared',
        'suggested_p_value_cutoff': 'suggestedPValueCutoff'
    }

    def __init__(self, adjusted_r_squared=None, error_sum_squares=None, intercept=None, intercept_standard_error=None, is_uncertain=False, regression_sum_squares=None, rsquared=None, suggested_p_value_cutoff=None):
        """
        RegressionOutputV1 - a model defined in Swagger
        """

        self._adjusted_r_squared = None
        self._error_sum_squares = None
        self._intercept = None
        self._intercept_standard_error = None
        self._is_uncertain = None
        self._regression_sum_squares = None
        self._rsquared = None
        self._suggested_p_value_cutoff = None

        if adjusted_r_squared is not None:
          self.adjusted_r_squared = adjusted_r_squared
        if error_sum_squares is not None:
          self.error_sum_squares = error_sum_squares
        if intercept is not None:
          self.intercept = intercept
        if intercept_standard_error is not None:
          self.intercept_standard_error = intercept_standard_error
        if is_uncertain is not None:
          self.is_uncertain = is_uncertain
        if regression_sum_squares is not None:
          self.regression_sum_squares = regression_sum_squares
        if rsquared is not None:
          self.rsquared = rsquared
        if suggested_p_value_cutoff is not None:
          self.suggested_p_value_cutoff = suggested_p_value_cutoff

    @property
    def adjusted_r_squared(self):
        """
        Gets the adjusted_r_squared of this RegressionOutputV1.
        The measure of how close the data is to the regression line, adjusted for the number of input signals and samples

        :return: The adjusted_r_squared of this RegressionOutputV1.
        :rtype: float
        """
        return self._adjusted_r_squared

    @adjusted_r_squared.setter
    def adjusted_r_squared(self, adjusted_r_squared):
        """
        Sets the adjusted_r_squared of this RegressionOutputV1.
        The measure of how close the data is to the regression line, adjusted for the number of input signals and samples

        :param adjusted_r_squared: The adjusted_r_squared of this RegressionOutputV1.
        :type: float
        """
        if adjusted_r_squared is None:
            raise ValueError("Invalid value for `adjusted_r_squared`, must not be `None`")

        self._adjusted_r_squared = adjusted_r_squared

    @property
    def error_sum_squares(self):
        """
        Gets the error_sum_squares of this RegressionOutputV1.
        The standard error for the sum squares

        :return: The error_sum_squares of this RegressionOutputV1.
        :rtype: float
        """
        return self._error_sum_squares

    @error_sum_squares.setter
    def error_sum_squares(self, error_sum_squares):
        """
        Sets the error_sum_squares of this RegressionOutputV1.
        The standard error for the sum squares

        :param error_sum_squares: The error_sum_squares of this RegressionOutputV1.
        :type: float
        """
        if error_sum_squares is None:
            raise ValueError("Invalid value for `error_sum_squares`, must not be `None`")

        self._error_sum_squares = error_sum_squares

    @property
    def intercept(self):
        """
        Gets the intercept of this RegressionOutputV1.
        The constant offset to add. 0 if forceThroughZero was true. This is the intercept for the output signal rather than the individual coefficients.

        :return: The intercept of this RegressionOutputV1.
        :rtype: float
        """
        return self._intercept

    @intercept.setter
    def intercept(self, intercept):
        """
        Sets the intercept of this RegressionOutputV1.
        The constant offset to add. 0 if forceThroughZero was true. This is the intercept for the output signal rather than the individual coefficients.

        :param intercept: The intercept of this RegressionOutputV1.
        :type: float
        """
        if intercept is None:
            raise ValueError("Invalid value for `intercept`, must not be `None`")

        self._intercept = intercept

    @property
    def intercept_standard_error(self):
        """
        Gets the intercept_standard_error of this RegressionOutputV1.
        The standard error for the intercept

        :return: The intercept_standard_error of this RegressionOutputV1.
        :rtype: float
        """
        return self._intercept_standard_error

    @intercept_standard_error.setter
    def intercept_standard_error(self, intercept_standard_error):
        """
        Sets the intercept_standard_error of this RegressionOutputV1.
        The standard error for the intercept

        :param intercept_standard_error: The intercept_standard_error of this RegressionOutputV1.
        :type: float
        """
        if intercept_standard_error is None:
            raise ValueError("Invalid value for `intercept_standard_error`, must not be `None`")

        self._intercept_standard_error = intercept_standard_error

    @property
    def is_uncertain(self):
        """
        Gets the is_uncertain of this RegressionOutputV1.
        True if this regression is uncertain

        :return: The is_uncertain of this RegressionOutputV1.
        :rtype: bool
        """
        return self._is_uncertain

    @is_uncertain.setter
    def is_uncertain(self, is_uncertain):
        """
        Sets the is_uncertain of this RegressionOutputV1.
        True if this regression is uncertain

        :param is_uncertain: The is_uncertain of this RegressionOutputV1.
        :type: bool
        """
        if is_uncertain is None:
            raise ValueError("Invalid value for `is_uncertain`, must not be `None`")

        self._is_uncertain = is_uncertain

    @property
    def regression_sum_squares(self):
        """
        Gets the regression_sum_squares of this RegressionOutputV1.
        The measure of how well the model matches the target

        :return: The regression_sum_squares of this RegressionOutputV1.
        :rtype: float
        """
        return self._regression_sum_squares

    @regression_sum_squares.setter
    def regression_sum_squares(self, regression_sum_squares):
        """
        Sets the regression_sum_squares of this RegressionOutputV1.
        The measure of how well the model matches the target

        :param regression_sum_squares: The regression_sum_squares of this RegressionOutputV1.
        :type: float
        """
        if regression_sum_squares is None:
            raise ValueError("Invalid value for `regression_sum_squares`, must not be `None`")

        self._regression_sum_squares = regression_sum_squares

    @property
    def rsquared(self):
        """
        Gets the rsquared of this RegressionOutputV1.

        :return: The rsquared of this RegressionOutputV1.
        :rtype: float
        """
        return self._rsquared

    @rsquared.setter
    def rsquared(self, rsquared):
        """
        Sets the rsquared of this RegressionOutputV1.

        :param rsquared: The rsquared of this RegressionOutputV1.
        :type: float
        """

        self._rsquared = rsquared

    @property
    def suggested_p_value_cutoff(self):
        """
        Gets the suggested_p_value_cutoff of this RegressionOutputV1.
        The value which the regression method suggests for ignoring coefficients

        :return: The suggested_p_value_cutoff of this RegressionOutputV1.
        :rtype: float
        """
        return self._suggested_p_value_cutoff

    @suggested_p_value_cutoff.setter
    def suggested_p_value_cutoff(self, suggested_p_value_cutoff):
        """
        Sets the suggested_p_value_cutoff of this RegressionOutputV1.
        The value which the regression method suggests for ignoring coefficients

        :param suggested_p_value_cutoff: The suggested_p_value_cutoff of this RegressionOutputV1.
        :type: float
        """
        if suggested_p_value_cutoff is None:
            raise ValueError("Invalid value for `suggested_p_value_cutoff`, must not be `None`")

        self._suggested_p_value_cutoff = suggested_p_value_cutoff

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, RegressionOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

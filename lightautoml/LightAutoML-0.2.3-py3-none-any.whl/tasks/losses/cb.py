"""Metrics and loss functions for Catboost."""

from typing import Callable, Union, Optional, Dict

import numpy as np
from log_calls import record_history

from .base import Loss


@record_history(enabled=False)
def cb_str_loss_wrapper(name, **params):
    return name + ':' + ';'.join([k + '=' + str(v) for (k, v) in params.items()])


@record_history(enabled=False)
def fw_rmsle(x, y): return np.log1p(x), y


_cb_loss_mapping = {
    'mse': ('RMSE', None, None),
    'mae': ('MAE', None, None),
    'logloss': ('Logloss', None, None),
    'rmsle': ('RMSE', fw_rmsle, np.expm1),
    'mape': ('MAPE', None, None),
    'quantile': ('Quantile', None, None),
    'fair': ('FairLoss', None, None),
    'huber': ('Huber', None, None),
    'crossentropy': ('MultiClass', None, None)
}

_cb_loss_params_mapping = {
    'quantile': {
        'q': 'alpha'
    },
    'huber': {
        'a': 'delta'
    },
    'fair': {
        'c': 'smoothness'
    }
}

_cb_metrics_dict = {
    'auc': 'AUC',
    'mse': 'RMSE',
    'mae': 'MAE',
    'r2': 'R2',
    'accuracy': 'Accuracy',
    'logloss': 'Logloss',
    'rmsle': 'MSLE',
    'mape': 'MAPE',
    'quantile': 'Quantile',
    'fair': 'FairLoss',
    'huber': 'Huber'
}

_cb_multiclass_metrics_dict = {
    'accuracy': 'Accuracy',
    'crossentropy': 'MultiClass',
    'f1_macro': 'TotalF1:average=Macro',
    'f1_micro': 'TotalF1:average=Micro',
    'f1_weighted': 'TotalF1:average=Weighted'
}

_cb_metric_params_mapping = {
    'quantile': {
        'q': 'alpha'
    },
    'huber': {
        'a': 'delta'
    },
    'fair': {
        'c': 'smoothness'
    }
}


@record_history(enabled=False)
class CBLoss(Loss):
    """Loss used for CatBoost."""

    def __init__(self, loss: Union[str, Callable], loss_params: Optional[Dict] = None,
                 fw_func: Optional[Callable] = None, bw_func: Optional[Callable] = None):
        """
        # TODO: docstring
        Args:
            loss: String with one of default losses.


            loss_params: additional loss parameters. \
                Format like in lightautoml.tasks.custom_metrics.
            fw_func: forward transformation. \
                Used for transformation of target and item weights.
            bw_func: backward transformation. \
                Used for predict values transformation.

        """
        self.loss_params = {}
        if loss_params is not None:
            self.loss_params = loss_params

        if type(loss) is str:
            if loss in _cb_loss_mapping:
                loss_name, fw_func, bw_func = _cb_loss_mapping[loss]
                if loss in _cb_loss_params_mapping:
                    mapped_params = {_cb_loss_params_mapping[loss][k]: v for (k, v) in self.loss_params.items()}
                    self.fobj = None
                    self.fobj_name = cb_str_loss_wrapper(loss_name, **mapped_params)

                else:
                    self.fobj = None
                    self.fobj_name = loss_name
            else:
                raise ValueError('Unexpected loss for catboost')
                # special loss for catboost, that is not defined in _cb_loss_mapping
                # self.fobj = None
                # self.fobj_name = loss
        else:
            # custom catboost objective
            self.fobj = loss
            self.fobj_name = None

        if fw_func is not None:
            self._fw_func = fw_func

        if bw_func is not None:
            self._bw_func = bw_func

        self.fobj_params = {}
        if loss_params is not None:
            self.fobj_params = loss_params

        self.metric = None
        self.metric_name = None

    def set_callback_metric(self, metric: Union[str, Callable], greater_is_better: Optional[bool] = None,
                            metric_params: Optional[Dict] = None):
        """
        Callback metric setter.

        Args:
            metric: callback metric.
            greater_is_better: whether or not higher value is better.
            metric_params: additional metric parameters.

        """
        # TODO: for what cb_utils
        # How to say that this metric is special class if there any task type?

        self.metric_params = {}
        if metric_params is not None:
            self.metric_params = metric_params

        if type(metric) is str:
            self.metric = None
            if metric in _cb_metrics_dict:
                if metric in _cb_metric_params_mapping:
                    metric_params = {_cb_metric_params_mapping[metric][k]: v for (k, v) in self.metric_params.items()}
                    self.metric_name = cb_str_loss_wrapper(_cb_metrics_dict[metric], **metric_params)
                else:
                    self.metric_name = _cb_metrics_dict[metric]
            elif metric in _cb_multiclass_metrics_dict:
                self.metric_name = _cb_multiclass_metrics_dict[metric]
        else:
            # TODO: Check it later
            self.metric_name = self.fobj_name
            self.metric_params = self.fobj_params
            self.metric = None

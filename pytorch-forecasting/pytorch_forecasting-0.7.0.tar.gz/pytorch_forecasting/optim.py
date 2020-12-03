"""
Optimizers not provided by PyTorch natively.
"""
import math
from typing import Any, Callable, Dict, Iterable, Optional, Tuple, Union

import torch
from torch.optim.optimizer import Optimizer

Params = Union[Iterable[torch.Tensor], Iterable[dict]]

LossClosure = Callable[[], float]
OptLossClosure = Optional[LossClosure]
Betas2 = Tuple[float, float]
State = Dict[str, Any]
OptFloat = Optional[float]
Nus2 = Tuple[float, float]


class Ranger(Optimizer):
    """
    Implements Ranger optimization algorithm (Lookahead with RAdam).

    Implementation is modified version from ``pytorch-ranger`` package which build upon
    its `original implementation <https://github.com/lessw2020/Ranger-Deep-Learning-Optimizer>`_.
    Ranger seems to be benefiting most models.

    Args:
        params: iterable of parameters to optimize or dicts defining
            parameter groups
        lr: learning rate (default: 1e-3)
        alpha: linear interpolation factor. 1.0 recovers the inner optimizer.
            (default: 0.5)
        k: number of lookahead steps (default: 6)
        N_sma_threshhold: Maximum length of the simple moving average (SMA)
        betas: coefficients used for computing
            running averages of gradient and its square (default: (0.95, 0))
        eps: term added to the denominator to improve
            numerical stability (default: 1e-8)
        weight_decay: weight decay (L2 penalty) (default: 0)

    Example:
        >>> from pytorch_forecasting.optim import Ranger
        >>> optimizer =  Ranger(model.parameters(), lr=0.1)
        >>> optimizer.zero_grad()
        >>> loss_fn(model(input), target).backward()
        >>> scheduler = StepLR(optimizer, step_size=1, gamma=0.7)
        >>> optimizer.step()
        >>> scheduler.step()
    """

    def __init__(
        self,
        params: Params,
        lr: float = 1e-3,
        alpha: float = 0.5,
        k: int = 6,
        N_sma_threshhold: int = 5,
        betas: Betas2 = (0.95, 0.999),
        eps: float = 1e-5,
        weight_decay: float = 0,
    ):
        # parameter checks
        if not 0.0 <= alpha <= 1.0:
            raise ValueError("Invalid slow update rate: {}".format(alpha))
        if not 1 <= k:
            raise ValueError("Invalid lookahead steps: {}".format(k))
        if not lr > 0:
            raise ValueError("Invalid Learning Rate: {}".format(lr))
        if not eps > 0:
            raise ValueError("Invalid eps: {}".format(eps))

        # parameter comments:
        # beta1 (momentum) of .95 seems to work better than .90...
        # N_sma_threshold of 5 seems better in testing than 4.
        # In both cases, worth testing on your dataset (.90 vs .95, 4 vs 5) to
        # make sure which works best for you.

        # prep defaults and init torch.optim base
        defaults = dict(
            lr=lr,
            alpha=alpha,
            k=k,
            step_counter=0,
            betas=betas,
            N_sma_threshhold=N_sma_threshhold,
            eps=eps,
            weight_decay=weight_decay,
        )
        super().__init__(params, defaults)

        # adjustable threshold
        self.N_sma_threshhold = N_sma_threshhold

        # now we can get to work...
        # removed as we now use step from RAdam...no need for
        # duplicate step counting
        # for group in self.param_groups:
        #    group["step_counter"] = 0
        # print("group step counter init")

        # look ahead params
        self.alpha = alpha
        self.k = k

        # radam buffer for state
        self.radam_buffer = [[None, None, None] for ind in range(10)]

        # self.first_run_check=0

        # lookahead weights
        # 9/2/19 - lookahead param tensors have been moved to state storage.
        # This should resolve issues with load/save where weights were left in
        # GPU memory from first load, slowing down future runs.

        # self.slow_weights = [[p.clone().detach() for p in group['params']]
        #                     for group in self.param_groups]

        # don't use grad for lookahead weights
        # for w in it.chain(*self.slow_weights):
        #    w.requires_grad = False

    def __setstate__(self, state: dict) -> None:
        super().__setstate__(state)

    def step(self, closure: OptLossClosure = None) -> OptFloat:
        r"""Performs a single optimization step.
        Arguments:
            closure: A closure that reevaluates the model and returns the loss.
        """
        _ = closure()
        loss = None
        # note - below is commented out b/c I have other work that passes back
        # the loss as a float, and thus not a callable closure.
        # Uncomment if you need to use the actual closure...

        # if closure is not None:
        # loss = closure()
        # Evaluate averages and grad, update param tensors
        for group in self.param_groups:

            for p in group["params"]:
                if p.grad is None:
                    continue
                grad = p.grad.data.float()
                if grad.is_sparse:
                    raise RuntimeError("Ranger optimizer does not support " "sparse gradients")

                p_data_fp32 = p.data.float()

                state = self.state[p]  # get state dict for this param

                if len(state) == 0:  # if first time to run...init dictionary
                    # with our desired entries
                    # if self.first_run_check==0:
                    # self.first_run_check=1
                    # print("Initializing slow buffer...should not see this
                    # at load from saved model!")
                    state["step"] = 0
                    state["exp_avg"] = torch.zeros_like(p_data_fp32)
                    state["exp_avg_sq"] = torch.zeros_like(p_data_fp32)

                    # look ahead weight storage now in state dict
                    state["slow_buffer"] = torch.empty_like(p.data)
                    state["slow_buffer"].copy_(p.data)

                else:
                    state["exp_avg"] = state["exp_avg"].type_as(p_data_fp32)
                    state["exp_avg_sq"] = state["exp_avg_sq"].type_as(p_data_fp32)

                # begin computations
                exp_avg, exp_avg_sq = state["exp_avg"], state["exp_avg_sq"]
                beta1, beta2 = group["betas"]

                # compute variance mov avg
                exp_avg_sq.mul_(beta2).addcmul_(grad, grad, value=1 - beta2)
                # compute mean moving avg
                exp_avg.mul_(beta1).add_(grad, alpha=1 - beta1)

                state["step"] += 1

                buffered = self.radam_buffer[int(state["step"] % 10)]
                if state["step"] == buffered[0]:
                    N_sma, step_size = buffered[1], buffered[2]
                else:
                    buffered[0] = state["step"]
                    beta2_t = beta2 ** state["step"]
                    N_sma_max = 2 / (1 - beta2) - 1
                    N_sma = N_sma_max - 2 * state["step"] * beta2_t / (1 - beta2_t)
                    buffered[1] = N_sma
                    if N_sma > self.N_sma_threshhold:
                        step_size = math.sqrt(
                            (1 - beta2_t)
                            * (N_sma - 4)
                            / (N_sma_max - 4)
                            * (N_sma - 2)
                            / N_sma
                            * N_sma_max
                            / (N_sma_max - 2)
                        ) / (1 - beta1 ** state["step"])
                    else:
                        step_size = 1.0 / (1 - beta1 ** state["step"])
                    buffered[2] = step_size

                if group["weight_decay"] != 0:
                    p_data_fp32.add_(p_data_fp32, alpha=-group["weight_decay"] * group["lr"])

                if N_sma > self.N_sma_threshhold:
                    denom = exp_avg_sq.sqrt().add_(group["eps"])
                    p_data_fp32.addcdiv_(exp_avg, denom, value=-step_size * group["lr"])
                else:
                    p_data_fp32.add_(exp_avg, alpha=-step_size * group["lr"])

                p.data.copy_(p_data_fp32)

                # integrated look ahead...
                # we do it at the param level instead of group level
                if state["step"] % group["k"] == 0:
                    slow_p = state["slow_buffer"]  # get access to slow param tensor
                    slow_p.add_(p.data - slow_p, alpha=self.alpha)  # (fast weights - slow weights) * alpha
                    p.data.copy_(slow_p)  # copy interpolated weights to RAdam param tensor
        return loss

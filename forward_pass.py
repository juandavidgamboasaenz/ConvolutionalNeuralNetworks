import numpy as np


def loss(y, x, w1, w2, w3, b1, b2, b3):
    w1.T = w1
    w2.T = w2
    w3.T = w3
    sys_loss = -np.log(
            np.sum(
                y * np.exp(
                    np.dot(
                        np.maximum(
                            0,
                            np.dot(
                                0,
                                np.dot(
                                    x,
                                    w1.T
                                ) + b1
                            ),
                            w2.T
                        ) + b2
                    ),
                    w3.T
                ) + b3
            ) /
            np.sum(
                np.exp(
                    np.dot(
                        np.maximum(
                            0,
                            np.dot(
                                np.maximum(
                                    0,
                                    np.dot(
                                        x,
                                        w1.T
                                    ) + b1
                                ),
                                w2.T
                            ) + b2
                        ),
                        w3.T
                    ) + b3
                ),
                axis=1,
                keepdims=True
            )
        )

    return sys_loss




#%%

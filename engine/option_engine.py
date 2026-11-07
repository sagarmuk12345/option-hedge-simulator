def call_intrinsic_value(
    stock_price,
    strike_price
):

    return max(
        stock_price - strike_price,
        0
    )


def put_intrinsic_value(
    stock_price,
    strike_price
):

    return max(
        strike_price - stock_price,
        0
    )


def call_profit(
    stock_price,
    strike_price,
    premium,
    contracts
):

    intrinsic = call_intrinsic_value(
        stock_price,
        strike_price
    )

    return (
        intrinsic - premium
    ) * contracts * 100


def put_profit(
    stock_price,
    strike_price,
    premium,
    contracts
):

    intrinsic = put_intrinsic_value(
        stock_price,
        strike_price
    )

    return (
        intrinsic - premium
    ) * contracts * 100
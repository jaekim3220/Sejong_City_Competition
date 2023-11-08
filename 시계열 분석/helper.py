from pandas import DataFrame, MultiIndex, concat, DatetimeIndex, Series
#--------------------------------------------------
# 모듈 불러오기
# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))
# from helper import normality_test, equal_variance_test, independence_test, all_test
#--------------------------------------------------

def set_datetime_index(df, field=None, inplace=False):
    """
        데이터 프레임의 인덱스를 datetime 형식으로 변환
        Parameters
        -------
        - df: 데이터 프레임
        - inplace: 원본 데이터 프레임에 적용 여부
        Returns
        -------
        - 인덱스가 datetime 형식으로 변환된 데이터 프레임
    """

    if inplace:
        if field is not None:
            df.set_index(field, inplace=True)

        df.index = DatetimeIndex(df.index.values, freq=df.index.inferred_freq)
        df.sort_index(inplace=True)
    else:
        cdf = df.copy()

        if field is not None:
            cdf.set_index(field, inplace=True)

        cdf.index = DatetimeIndex(cdf.index.values, freq=cdf.index.inferred_freq)
        cdf.sort_index(inplace=True)
        return cdf
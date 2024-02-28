import xarray as xr
import numpy as np
import pandas as pd


def get_annotation_table(ds, dim="sample"):
    """
    return a copy of the peptide table after converting all
    the data types applying the pandas NaN heuristic

    Parameters
    ----------

    ds : xarray.DataSet
        The dataset to extract an annotation from.

    dim : str
        The annotation table to grab: "sample" or "peptide".

    Returns
    -------

    pd.DataFrame :
        The annotation table.

    """

    st = ds[f"{dim}_table"].to_pandas().convert_dtypes()
    st.index.name = f"{dim}_id"
    return st


def id_query(ds, query, dim="sample"):
    """
    Apply a sample or peptide query statement to the
    entire dataset and retrieve the respective indices.

    Note
    ----
    For more on pandas queries, see
    https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html

    Parameters
    ----------

    ds : xarray.DataSet
        The dataset you would like to query.

    query : str
        pandas query expression

    dim : str


    Return
    ------
    list[int] :
        The list of integer identifiers that apply to a given expression
        for the respective dimension.
    """

    return get_annotation_table(ds, dim).query(query, engine='python').index.values


def csv_to_ds(csv_dir, prefix):
    """
    Constructs an xarray object from a set of CSV files corresponding
    to peptide annotations, sample annotations, and peptide-related
    quantities.

    Note
    ----
    The expected CSV files are fixed.


    Parameters
    ----------

    csv_dir : str
        Directory of CSV files.

    prefix : str
        Dataset name that forms the prefix to the CSV file names.

    
    Return
    ------
        An xarray object encapsulating the data from the CSV files.
    """
    peptide_table_file = f'{csv_dir}/{prefix}_peptide_annotation_table.csv'
    peptide_table_df = pd.read_csv(peptide_table_file,index_col='peptide_id')
    peptide_table_arr = xr.DataArray(data=peptide_table_df, dims=['peptide_id','peptide_metadata'], name='peptide_table')
    peptide_table_ds = peptide_table_arr.to_dataset()

    sample_table_file = f'{csv_dir}/{prefix}_sample_annotation_table.csv'
    sample_table_df  = pd.read_csv(sample_table_file,index_col='sample_id')
    sample_table_arr = xr.DataArray(data=sample_table_df, dims=['sample_id','sample_metadata'], name='sample_table')
    sample_table_ds = sample_table_arr.to_dataset()

    counts_file = f'{csv_dir}/{prefix}_counts.csv'
    counts_df = pd.read_csv(counts_file,index_col=0)
    counts_df.columns = counts_df.columns.astype(int)
    counts_arr = xr.DataArray(data=counts_df, dims=['peptide_id','sample_id'], name='counts')
    counts_ds = counts_arr.to_dataset()

    cpm_file = f'{csv_dir}/{prefix}_cpm.csv'
    cpm_df = pd.read_csv(cpm_file,index_col=0)
    cpm_df.columns = cpm_df.columns.astype(int)
    cpm_arr = xr.DataArray(data=cpm_df, dims=['peptide_id','sample_id'], name='cpm')
    cpm_ds = cpm_arr.to_dataset()

    enrichment_file = f'{csv_dir}/{prefix}_enrichment.csv'
    enrichment_df = pd.read_csv(enrichment_file,index_col=0)
    enrichment_df.columns = enrichment_df.columns.astype(int)
    enrichment_arr = xr.DataArray(data=enrichment_df, dims=['peptide_id','sample_id'], name='enrichment')
    enrichment_ds = enrichment_arr.to_dataset()

    smooth_diff_sel_file = f'{csv_dir}/{prefix}_smooth_flank_1_scaled_diff_sel.csv'
    smooth_diff_sel_df = pd.read_csv(smooth_diff_sel_file,index_col=0)
    smooth_diff_sel_df.columns = smooth_diff_sel_df.columns.astype(int)
    smooth_diff_sel_arr = xr.DataArray(data=smooth_diff_sel_df, dims=['peptide_id','sample_id'], name='smooth_flank_1_scaled_diff_sel')
    smooth_diff_sel_ds = smooth_diff_sel_arr.to_dataset()

    diff_sel_file = f'{csv_dir}/{prefix}_diff_sel.csv'
    diff_sel_df = pd.read_csv(diff_sel_file,index_col=0)
    diff_sel_df.columns = diff_sel_df.columns.astype(int)
    diff_sel_arr = xr.DataArray(data=diff_sel_df, dims=['peptide_id','sample_id'], name='diff_sel')
    diff_sel_ds = diff_sel_arr.to_dataset()

    return xr.merge([peptide_table_ds, sample_table_ds, counts_ds, cpm_ds, enrichment_ds, smooth_diff_sel_ds, diff_sel_ds])



from fit import *
from pathlib import Path
from utils import save_df
from config import ALL_NS_DATA_PATH

fileid = int(sys.argv[1])
ns_df_paths = sorted(ALL_NS_DATA_PATH.iterdir())
ns_df_paths = [p for p in ns_df_paths if p.name[0].isnumeric()]
ev_df_pkl = ns_df_paths[fileid]
print('Reconstructing ' + ev_df_pkl.name)
df = pd.read_pickle(ev_df_pkl)
fit_df = dataframe_fit(df)
save_df(fit_df,'fit_' + ev_df_pkl.name, ev_df_pkl.parent)


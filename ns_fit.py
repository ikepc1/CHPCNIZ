from fit import *
from pathlib import Path
from utils import save_df
from config import ALL_NS_DATA_PATH

fileid = int(sys.argv[1])
ns_df_paths = sorted(ALL_NS_DATA_PATH.iterdir())
all_ns_df_paths = [p for p in ns_df_paths if p.name[0].isnumeric()]
already_fit_paths = [p for p in ns_df_paths if p.name.startswith('fit')]
already_fit_names = [p.name[4:] for p in already_fit_paths]
ns_to_fit = [p for p in all_ns_df_paths if p.name not in already_fit_names]
ev_df_pkl = ns_to_fit[fileid]
print('Reconstructing ' + ev_df_pkl.name)
df = pd.read_pickle(ev_df_pkl)
fit_df = dataframe_fit(df)
save_df(fit_df,'fit_' + ev_df_pkl.name, ev_df_pkl.parent)


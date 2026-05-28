# Data

Raw data is not stored in this repository.

The notebook downloads the Australian Election 2019 Tweets dataset from Kaggle using `kagglehub`:

```python
import kagglehub
path = kagglehub.dataset_download('taniaj/australian-election-2019-tweets')
```

Expected primary CSV file:

```text
auspol2019.csv
```

Keep large raw files outside GitHub unless required by the instructor.

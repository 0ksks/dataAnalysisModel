from torch.utils.data import Dataset
import numpy as np
class __DatasetName(Dataset):
    def __init__(self, params=None) -> None:
        self.data = np.random.randint(1,10,(100,2))
    def __len__(self) -> int:
        return self.data.shape[0]
    def __getitem__(self, index):
        return self.data.__getitem__(index)

def get_dataset(params=None) -> __DatasetName:
    __datasetName = __DatasetName(params)
    return __datasetName

if __name__ == "__main__":
    datasetName = __DatasetName()
    print(f"{len(datasetName) = }")
    print(f"{datasetName[1:5] = }")
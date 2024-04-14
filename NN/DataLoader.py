from DataSet import get_dataset as __get_dataset
from torch.utils.data import random_split, DataLoader, Subset
import torch
from typing import Union

DATASET_PARAMS = None
BATCH_SIZE = 10
SHUFFLE = True
RANDOM_SEED = 2003

def split_dataloader(
    ratio:tuple=(8, 1, 1),
    batchSize:Union[int, list[int]]=BATCH_SIZE,
    shuffle=SHUFFLE,
    datasetParams=DATASET_PARAMS,
    generator=torch.Generator().manual_seed(RANDOM_SEED)
    ) -> list[DataLoader]:
    print(f"split by {ratio}")
    if isinstance(batchSize, int):
        batchSize = [batchSize,]*3
    ratio = list(map(lambda x:x/sum(ratio), ratio))
    ratio[-1] = 1 - sum(ratio[:-1])
    datasets = random_split(__get_dataset(datasetParams), ratio, generator)
    dataloaders = []
    for idx, dataset in enumerate(datasets):
        if idx==0:
            dataloaders.append(DataLoader(dataset, batchSize[idx], shuffle))
        else:
            dataloaders.append(DataLoader(dataset, batchSize[idx]))
    return dataloaders

def mini_dataloader(dataloader:DataLoader, subSize=100, subBatchSize=10, subShuffle=True):
    oriDataset = dataloader.dataset
    oriDataSize = len(oriDataset)
    import random
    randomIndices = random.sample(range(oriDataSize), subSize)
    return DataLoader(Subset(oriDataset, randomIndices), subBatchSize, shuffle=subShuffle)

if __name__ == "__main__":
    split_dataloader()
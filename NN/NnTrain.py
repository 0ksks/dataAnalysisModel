def kernel(hyperParams=None):
    from DataLoader import split_dataloader, mini_dataloader
    from NnStructure import ModelName
    import pytorch_lightning as pl
    model = ModelName()
    trainer = pl.Trainer()
    loaders = split_dataloader()
    trainer.fit(model, loaders[0])
    train_loss = trainer.callback_metrics["train_loss"].item()
    return train_loss
if __name__ == "__main__":
    kernel()
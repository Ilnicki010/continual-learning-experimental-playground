# from datasets.base_dataset import get_transform
from datasets.base_dataset import BaseDataset
import torch
import torchvision


class CIFAR10Dataset(torchvision.datasets.CIFAR10):
    def __init__(self, configuration):
        super().__init__(**configuration["pytorch_dataset_config"])

    def __getitem__(self, index):
        # get source image as x
        # get labels as y
        return x, y

    def __len__(self):
        # return the size of the dataset
        return 1

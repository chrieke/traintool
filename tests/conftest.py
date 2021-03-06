import sys
import os
import numpy as np
import torchvision
import torch
from typing import Union, List


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def create_image_classification_data(
    output_format: str = "numpy",
    grayscale: bool = True,
    num_samples: int = 4,
    seed: int = 0,
) -> Union[List[np.ndarray], torch.utils.data.Dataset]:
    """
    Create fake data for image classification, including images (values from 0 to 1) 
    and labels (10 classes). 

    Args:
        output_format (str, optional): "numpy" (for list of numpy arrays 
            [images, labels]) or "torch" (for torch.utils.data.Dataset). Defaults to 
            "numpy".
        grayscale (bool, optional): If True, images are grayscale and of size 28x28, 
            otherwise they have 3 color channels and are 224x224. Defaults to False.
        num_samples (int, optional): Number of samples in the dataset. Defaults to 4.
        seed (int, optional): Seed for data generation. Defaults to 0.

    Returns:
        Union[List[np.ndarray], torch.utils.data.Dataset]: The generated fake data. 
    """

    # Create raw data (seeded, so always the same data).
    np.random.seed(seed)
    if grayscale:
        images = np.random.rand(num_samples, 1, 28, 28)
    else:
        images = np.random.rand(num_samples, 3, 224, 224)
    labels = np.random.randint(10, size=num_samples)

    # Convert to correct output format.
    if output_format == "numpy":
        return [images, labels]
    elif output_format == "torch":
        dataset = torch.utils.data.TensorDataset(
            torch.from_numpy(images).float(), torch.from_numpy(labels).long(),
        )
        return dataset

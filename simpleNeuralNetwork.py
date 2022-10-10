from torch.utils.data import DataLoader,Dataset
import matplotlib.pyplot as plt
import numpy as np
import torch
import pandas as pd
import torch.nn as nn
class MyDataSet(Dataset):
    def __init__(self):
        self.labels=  None

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return self.labels[idx]

# train_dataLoader = DataLoader(train, batch_size=64,shuffle=True )
device = "cuda" if torch.cuda.is_available() else "cpu"

class Network(nn.Module):
    def __init__(self):
        super(Network,self).__init__()
        self.flatten = nn.Flatten()
        self.liner_relu_stack = nn.Sequential(
            nn.Linear(28*28,512),
            nn.ReLU(),
            nn.Linear(512,512),
            nn.ReLU(),
            nn.Linear(512,10)
        )
    def forward(self,x):
        x = self.flatten(x)
        logits = self.liner_relu_stack(x)
        return logits

model = Network().to(device)
print(model)

x = torch.rand(1,28,28,device=device)


learning_rate = 1e-3
batch_size = 64
epochs = 5
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(),lr=learning_rate)


def train_loop(dataLoader, model, loss_fn, optimizer):
    size = len(dataLoader.dataset)
    for batch, (X, y) in enumerate(dataLoader):
        pred = model(X)
        loss = loss_fn(pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if batch % 200:
            loss, current = loss.item(), batch *len(X)
            print(loss, current)

def test_loop(dataLoader, model, loss_fn, optimizer):
    size = len(dataLoader.dataset)
    num_batchs = len(dataLoader)
    test_loss, correct = 0, 0

    with torch.no_grad():
        for X, y in enumerate(dataLoader):
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()

    test_loss /= num_batchs
    correct /= size

for epoch in range(epochs):
    print(f"______eopch:{epoch}_____")
    # train_loop(dataLoader, model, loss_fn, optimizer)
    # test_loop(dataLoader, model, loss_fn, optimizer)

torch.save(model.state_dict(),"ttt.pth")





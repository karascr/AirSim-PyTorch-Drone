#!/usr/bin/env python
"""Run DQN AirSim quadrotor

- Author: Subin Yang
- Contact: subinlab.yang@gmail.com
"""
from agent import Agent

if __name__ == "__main__":
    agent = Agent(useGPU=True, useDepth=True)
    agent.train()

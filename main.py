# -*- coding: utf-8 -*-
"""
TODO: Add Docs
"""

from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

from fastapi import FastAPI

import subprocess

app = FastAPI()


@app.get("/")
def index():
    generate_diagram()
    subprocess.run(["ls", "-l"])
    return {"message": "OK"}


def generate_diagram():
    with Diagram("Grouped Workers", filename="diagram", show=False, direction="TB"):
        (
            ELB("lb")
            >> [
                EC2("worker1"),
                EC2("worker2"),
                EC2("worker3"),
                EC2("worker4"),
                EC2("worker5"),
            ]
            >> RDS("events")
        )

#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { Stack } from "../lib/stack";

const app = new cdk.App();
new Stack(app, "ServerStack", {});

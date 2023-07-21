#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { AccessesStack } from "../lib/accesses-stack";
import { ServerStack } from "../lib/server-stack";

const app = new cdk.App();
const accessesStack = new AccessesStack(app, "AccessesStack");
const serverStack = new ServerStack(app, "ServerStack", {});
serverStack.addDependency(accessesStack);

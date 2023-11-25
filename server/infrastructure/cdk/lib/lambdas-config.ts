import { readFileSync } from "fs";
import path = require("path");
import * as yaml from "js-yaml";
import { HttpMethod } from "@aws-cdk/aws-apigatewayv2-alpha";

export class LambdaConfigs {
  static getAll() {
    return LambdaConfigsStore.getConfigs();
  }

  static getEndpoints() {
    const configs = LambdaConfigsStore.getConfigs();

    return configs.filter((config) => config.type === LambdaType.Endpoint);
  }
}

class LambdaConfigsStore {
  private static configs: LambdaConfig[] = [];

  static getConfigs() {
    if (this.configs.length) {
      return this.copy();
    }

    this.configs = this.getFromSource();

    return this.copy();
  }

  private static copy() {
    return this.configs.map((config) => ({ ...config }));
  }

  private static getFromSource() {
    const rawConfigs = this.readConfigFile();
    const result: LambdaConfig[] = [];

    for (const lambdaName of Object.keys(rawConfigs)) {
      const rawConfig = rawConfigs[lambdaName];
      result.push({
        name: lambdaName,
        type: rawConfig.type as LambdaType,
        auth: rawConfig.auth as Auth,
        handlerFunc: rawConfig.handler_func,
        handlerModule: rawConfig.handler_module,
        method: rawConfig.method
          ? (rawConfig.method.toUpperCase() as HttpMethod)
          : undefined,
        path: rawConfig.path,
      });
    }

    return result;
  }

  private static readConfigFile() {
    const configFilePath = path.resolve(__dirname, "../../lambdas.yml");

    return yaml.load(readFileSync(configFilePath, "utf8")) as Record<
      string,
      RawLambdaConfig
    >;
  }
}

interface RawLambdaConfig {
  type: string;
  method: string;
  path: string;
  auth: string;
  handler_module: string;
  handler_func: string;
}

export interface LambdaConfig {
  name: string;
  type: LambdaType;
  method?: HttpMethod;
  path: string;
  auth?: Auth;
  handlerModule: string;
  handlerFunc: string;
}

enum LambdaType {
  Endpoint = "endpoint",
  Worker = "worker",
}
export enum Auth {
  ApiKey = "api-key",
  Cognito = "cognito",
}

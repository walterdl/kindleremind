export interface ApiKeysResponse {
  apiKeys: ApiKey[];
}

export interface ApiKey {
  value: string;
  name: string;
  /**
   * ISO 8601 UTC
   */
  createdAt: string;
}

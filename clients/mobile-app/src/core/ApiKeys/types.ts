export interface ApiKey {
  id: string;
  value: string;
  name: string;
  /**
   * ISO 8601 UTC
   */
  createdAt: string;
}

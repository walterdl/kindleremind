export interface Clipping {
  id: string;
  author: string;
  content: string;
  position: {
    location: string;
    page: string;
  };
  timestamp: string;
  title: string;
  type: ClippingType;
  key: number;
  user: string;
}

export enum ClippingType {
  Highlight = 'HIGHLIGHT',
  Bookmark = 'BOOKMARK',
}

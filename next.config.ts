import path from 'path';
import { NextConfig } from 'next';

const config: NextConfig = {
  turbopack: {
    root: path.resolve(__dirname),
  },
};

export default config;

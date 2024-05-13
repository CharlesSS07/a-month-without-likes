import { nodeResolve } from '@rollup/plugin-node-resolve';

export default {
   // make sure this points to your entry point file
  input: 'src/login.js',
  output: {
    dir: '../public/static',
    // Outputs to a native module format. This has good browser compatibility
    // but does not support IE11. Use 'iife' or researach fallback script
    // loading for IE11 support.
    format: 'esm',
  },
  plugins: [nodeResolve()]
};

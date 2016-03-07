import path from 'path';
import webpack from 'webpack';

const config = {

  // Gives you sourcemaps without slowing down rebundling
  devtool: 'eval-source-map',
  entry: path.join(__dirname, 'client/js/main.js'),
  // entry: './client/js/main.js',
  output: {
    path: path.join(__dirname, 'royalfilms/static/dist/'),
    // path: './royalfilms/static/dist/',
    filename: 'bundle.js',
    publicPath: '/static/'
  },
  module: {
    loaders: [
      {
        test: /\.js?$/,
        exclude: /node_modules/,
        loader: 'babel-loader'
      }
    ]
  },
  plugins: [
    new webpack.ProvidePlugin({
      'fetch': 'imports?this=>global!exports?global.fetch!whatwg-fetch'
    })
  ]
};

export default config;

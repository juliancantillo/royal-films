import path from 'path';

const config = {

  // Gives you sourcemaps without slowing down rebundling eval-source-map
  devtool: 'cheap-module-source-map',
  entry: path.join(__dirname, 'client/js/main.js'),
  output: {
    path: path.join(__dirname, 'royalfilms/static/dist/'),
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
    new webpack.optimize.UglifyJsPlugin(),
    new webpack.DefinePlugin({
      'process.env': {
        'NODE_ENV': JSON.stringify('production')
      }
    }),
    new webpack.ProvidePlugin({
      'fetch': 'imports?this=>global!exports?global.fetch!whatwg-fetch'
    })
  ]
};

export default config;

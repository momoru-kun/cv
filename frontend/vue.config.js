module.exports = {
  transpileDependencies: [
    'vuetify'
  ],
  outputDir: process.env.NODE_ENV === 'production' ? '../cv/static' : 'dist/',
  indexPath: process.env.NODE_ENV === 'production' ? '../../templates/index.html' : 'index.html',
  assetsDir: '',
  publicPath: process.env.NODE_ENV === 'production' ? 'static' : '/',
  devServer: {
    proxy: {
      '^/api': {
        target: 'http://localhost:8000/'
      }
    }
  }
}

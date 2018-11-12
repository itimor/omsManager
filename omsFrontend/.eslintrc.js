module.exports = {
  root: true,
  'extends': [
    'plugin:vue/essential',
    '@vue/standard'
  ],
  rules: {
    // allow async-await
    'generator-star-spacing': 'off',
    // allow debugger during development
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'vue/no-parsing-error': [2, { 'x-invalid-end-tag': false }],
    'no-undef': 'off',
    'no-tabs': 'off',
    '[vue]': {
      'edit.insertSpaces': true,
      'editor.tabSize': 2
    },
    "space-before-function-paren": ["error", "never"],
  }
}

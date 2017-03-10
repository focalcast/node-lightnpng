{
  'targets': [
    {
      'target_name': 'lightnpng',
      'include_dirs': ["<!(node -e \"require('nan')\")"],
      'sources': [
        'src/init.cc',
        'src/write_png.cc',
        'src/compress.cc'
      ],
      'xcode_settings': {
        'OTHER_CFLAGS': [
          '-stdlib=libc++'
        ],
      },
    }
  ]
}

define("songza/model-config", function() {
  var ModelConfig = {
    'station': {
      'radio_rules': {
        'min_artist_count': 8,
        'min_song_count': 20
       }
    },
    'situation': {
      'countries': [
          {'value': 'CA',  'label': 'Canada'            },
          {'value': 'US',  'label': 'The United States' }
      ],
      'devices': [
          {'value': 'android-phone',  'label': 'Android Phone'  },
          {'value': 'android-tablet', 'label': 'Android Tablet' },
          {'value': 'iphone',         'label': 'iPhone'         },
          {'value': 'ipad',           'label': 'iPad'           },
          {'value': 'sonos',          'label': 'Sonos'          },
          {'value': 'ubrowser',       'label': 'U Browser'      },
          {'value': 'web',            'label': 'Web'            },
          {'value': 'windows',        'label': 'Windows'        },
          {'value': 'windows-phone',  'label': 'Windows Phone'  }
      ],
      'dow': [
          {'value': 0,  'label': 'Sunday',    'day_value': 0 },
          {'value': 1,  'label': 'Monday',    'day_value': 1 },
          {'value': 2,  'label': 'Tuesday',   'day_value': 2 },
          {'value': 3,  'label': 'Wednesday', 'day_value': 3 },
          {'value': 4,  'label': 'Thursday',  'day_value': 4 },
          {'value': 5,  'label': 'Friday',    'day_value': 5 },
          {'value': 6,  'label': 'Saturday',  'day_value': 6 }
      ],
      'time_periods': [
          {'value': 0,  'label': 'Morning',      'hours_range': [4, 8]  },
          {'value': 1,  'label': 'Late Morning', 'hours_range': [9, 11] },
          {'value': 2,  'label': 'Afternoon',    'hours_range': [12, 16]},
          {'value': 3,  'label': 'Evening',      'hours_range': [17, 20]},
          {'value': 4,  'label': 'Night',        'hours_range': [21, 23]},
          {'value': 5,  'label': 'Late Night',   'hours_range': [0, 3]  }
      ],
      'modes': [
        
          {'value': 'general', 'label': 'General'},
        
          {'value': 'thanksgiving', 'label': 'Thanksgiving'},
        
          {'value': 'christmas', 'label': 'Christmas'}
        
      ]
    },
    'weather': {
      'defaults': {
        'min_temperature': -460,
        'max_temperature': 1000000,
        'min_humidity': 0,
        'max_humidity': 100,
        'sunrise_before': 30,
        'sunrise_after': 30,
        'sunset_before': 30,
        'sunset_after': 30
      }
    }
  };
  return ModelConfig;
});

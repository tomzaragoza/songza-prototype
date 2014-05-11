

/**
  @module songza-config
 */
/*global window */
define("songza/config", function() {
  "use strict";

  var Config = {
    debug: false,
    api: {
      root: "/api/1"
    },
    hashsignal: "web:2",
    // DOM Enhancements should be added last since
    // they are currently run the minute they are added
    // "songza/dom-enhancements/delete-shelves",
    default_plugins: [
      "songza/systems/facebook",
      "songza/systems/twitter",
      "songza/systems/google-analytics",
      "songza/systems/google-plus",
      "bklyn/songza/app-enhancements/browser-warning",
      "bklyn/songza/app-enhancements/apply-background-gradient",
      "bklyn/songza/app-enhancements/nav-and-subnav",
      "bklyn/songza/app-enhancements/key-capture",
      "bklyn/songza/app-enhancements/update-browser-title-with-current-song",
      "bklyn/songza/app-enhancements/debug-console-require",
      "bklyn/songza/app-enhancements/search-bar",
      "bklyn/songza/app-enhancements/recent-stations-for-user",
      "bklyn/songza/app-enhancements/init-favorites-manager",
      "bklyn/songza/app-enhancements/perfect-scrollbar",
      "bklyn/songza/app-enhancements/loading-screen-hiding",
      "bklyn/songza/dom-enhancements/playable-stations",
      "bklyn/songza/dom-enhancements/playlist-landing-self-hiding",
      "bklyn/songza/dom-enhancements/sharing",
      "bklyn/songza/dom-enhancements/favoritable",
      "bklyn/songza/dom-enhancements/buy-links",
      "bklyn/songza/dom-enhancements/back-links"
    ],
    club_plugins: [
      "songza/systems/facebook",
      "songza/systems/google-analytics",
      "songza/systems/google-plus",
      "songza/systems/comscore"
    ],
    site_custom_plugins: [
      
        // "songza/sites/songza/ads",
      
        // "songza/sites/songza/ad-preroll"
      
      "bklyn/songza/sites/songza/ads",
      "bklyn/songza/sites/songza/ad-preroll"
    ],
    adSlotConfig: [
      ["/refresh/advertising/top/",  970, 90,  "#ad-top"],
      ["/refresh/advertising/side/", 300, 600, "#ad-side", {fullplayerStatus: false}],
      ["/refresh/advertising/side/", 300, 600, "#ad-fullplayer", {fullplayerStatus: true}],
      ["/refresh/advertising/side/", 300, 600, "#ad-side-concierge-2", {fullplayerStatus: false, inCurrentConciergeView: true}],
      ["/refresh/advertising/side/", 300, 600, "#ad-side-concierge-3", {fullplayerStatus: false, inCurrentConciergeView: true}]
    ],
    site: "songza",
    name: "Songza",
    promo_product_list: ["android", "iphone", "web", "web-full"],
    static_url: '/static/a49667754413/',
    facebook: {
      app_id:      "125168500866352",
      permissions: "publish_actions,email"
    },
    chrome_cast: {
      v1_app_id: "Songza_App",
      v2_app_id: "852E49F8"
    },
    desk: {
      domain: "songza.desk.com"
    },
    olark: {
      site_id: ""
    },
    comscore: {
      client_id: "7515253"
    },
    google_analytics: {
      account_id: "UA-468380-14"
    },
    google_plus: {
      app_id: "820833903890.apps.googleusercontent.com",
      app_package_name: "com.ad60.songza"
    },
    twitter: {
      handle: "songza"
    },
    quantcast: {
      accounts: ["p-9bJw_uniA9hco", "p-61RSmkUm_qRRM"] 
    },
    getsatisfaction: {
      company: "songza"
    },
    disqus: {
      shortname: ""
    },
    soundManager: {
      url: '/static/a49667754413/swf/soundmanager/'
    },
    comment_provider: "facebook",
    
    features: {
        'systems.black_planet.auth':  false,
        'systems.facebook.auth':      true,
        'systems.facebook.share':     true,
        'systems.facebook.scrobbing': true,
        'systems.facebook.comment':   true,
        'systems.google.auth':        true,
        'systems.google.share':       true,
        'systems.songza.login':       true,
        'systems.songza.signup':      true,
        'songza.ad_preroll': true
    },
    dataFreshness: {
      /* How often should we refresh following lists */
      following: 4 * 60 * 60,
      /* How often should we refresh followers lists */
      followers: 4 * 60 * 60
    },
    timeouts: {
      /* How long to wait before displaying the page-loading throbber */
      pageNavigateProgress: 1000,
      /* How long to wait for a song to start to play before showing the song-buffer throbber */
      songLoadingProgress:  500,
      /* What intervals to poll for feeds at */
      feedPollIntervals:    [ [5 * 60, 5], [30 * 60] ],
      /* How long to wait before automatically sending "Station Listen" times to google-analytics */
      stationMaxIdleTime: 1 * 60 * 60,
      stationTotalPlayTime: 8 * 60 * 60,
      /* How long to wait before scrolling a shelf on mouseenter */
      shelfAutoScrollDelay: 250
    },
    makeAbsolute: function(path) {
      var server = window.location.protocol + "//" + window.location.host;

      return server + path;
    }
  };

  return Config;
});

// This file was automatically generated from ads.common.soy.
// Please don't edit this file by hand.

define('songza/templates/ads', [], function() {
if (typeof songza == 'undefined') { var songza = {}; }
if (typeof songza.templates == 'undefined') { songza.templates = {}; }
if (typeof songza.templates.ads == 'undefined') { songza.templates.ads = {}; }


songza.templates.ads.preRollModal = function(opt_data, opt_ignored) {
  return '<div class="modal"><div class="modal-body"></div><div class="modal-footer"><span class="station-name">' + soy.$$escapeHtml(opt_data.station.name) + '</span> will start playing 100% interruption free after these messages</div><div class="modal-upsell"></div></div>';
};


songza.templates.ads.providerVast = function(opt_data, opt_ignored) {
  return '<div class="szi-video"><div id="vast-video-ad-' + soy.$$escapeHtml(opt_data.view_id) + '"></div><div id="vast-video-ad-pause-message" class="hidden">Click below to resume this video</div></div><div class="szi-image"><div id="vast-image-ad-' + soy.$$escapeHtml(opt_data.view_id) + '"></div></div>';
};


songza.templates.ads.providerTargetSpot = function(opt_data, opt_ignored) {
  return '<div class="szi-ad"><div id="tspot_companion_ad_div"></div></div>';
};


songza.templates.ads.clubSongzaUpsell = function(opt_data, opt_ignored) {
  return '<a href="' + soy.$$escapeHtml(opt_data.href_url) + '" target="new" data-sz-no-route><img src="' + soy.$$escapeHtml(opt_data.image_url) + '" /></a>';
};

return songza.templates.ads;
});

(function($){
    'use strict';

    $.fn.gsearch = function(searchbox, submit) {
      var plugin = this,
        $searchbox = $(searchbox),
        $submit = $(submit);

      init: function() {
        $submit.click(plugin._on_submit_search);
      },

      _on_submit_search: function() {
        var q = $searchbox.val(),
          url = 'http://www.google.com/cse?cx=000888210889775888983:eeinzw5ta4e&q=truc&oq=truc&gs_l=partner.3...2837.3212.0.3373.0.0.0.0.0.0.0.0..0.0.gsnos%2Cn%3D13..0.0.343j58307j4..1ac.1.#gsc.tab=0&gsc.page=1&gsc.q=' + q;
        window.location = url;
        return false;
      }

      plugin.init();
    }
})(jQuery)

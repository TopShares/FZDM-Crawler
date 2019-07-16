import re

from lxml import etree
html = '''
<!DOCTYPE html>
<html>
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta http-equiv="Content-Language" content="utf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1" />
  <meta http-equiv="x-dns-prefetch-control" content="on" />
  <link rel="dns-prefetch" href="//www.fzdm.com" />
  <link rel="dns-prefetch" href="//manhua.fzdm.com" />
  <link rel="dns-prefetch" href="//p1.manhuapan.com" />
  <link rel="dns-prefetch" href="//p3.manhuapan.com" />
  <link rel="dns-prefetch" href="//p5.manhuapan.com" />
  <link rel="dns-prefetch" href="//p17.manhuapan.com" />
  <meta content="all" name="robots" />
  <title>七原罪漫画 七原罪319话 七原罪漫画连载 风之动漫</title>
  <meta name="keywords" content="七原罪漫画 七原罪319话 七原罪漫画连载 " />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <meta http-equiv="Cache-Control" content="no-transform" />
  <meta http-equiv="Cache-Control" content="no-siteapp" />
  <meta name="applicable-device" content="pc,mobile" />
  <meta name="HandheldFriendly" content="true" />
  <meta property="og:site_name" content="风之动漫" /> 
  <meta property="og:title" content="七原罪漫画" />
  <meta property="og:type" content="novel" />
  <meta property="og:novel:read_url" id="readurl" content="https://manhua.fzdm.com/56/" />
  <meta property="og:image" content="https:https://static.fzdm.com/none.png" />
  <meta property="og:description" content="风之动漫为您提供最新的七原罪漫画更新。七大罪," />
  <meta property="og:novel:category" content="" />
  <meta property="og:novel:author" content="" />
  <meta property="og:novel:book_name" content="七原罪" />
  <meta property="og:url" content="https://manhua.fzdm.com/56/" />
  <meta property="og:novel:status" content="" />
  <meta property="og:novel:update_time" content="2019-07-10" />
  <meta property="og:novel:latest_chapter_name" content="七原罪318话" />
  <meta property="og:novel:latest_chapter_url" content="https://manhua.fzdm.com/56/318/" /> 
  <!--[if lte IE 8]>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/fzdm/st@d24ab7c6533348334da08feaf462e72258d28fa7/pure/fzdm-old-ie7-min-490f867623.css">
<script type="text/javascript" src="https://cdn.jsdelivr.net/gh/fzdm/st@d24ab7c6533348334da08feaf462e72258d28fa7/js/pie/PIE_IE678.js"></script>
<![endif]-->
  <!--[if IE 8]>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/fzdm/st@d24ab7c6533348334da08feaf462e72258d28fa7/pure/fzdm-old-ie-min-b76be47263.css">
<![endif]-->
  <!--[if gt IE 8]><!-->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/fzdm/st@d24ab7c6533348334da08feaf462e72258d28fa7/pure/fzdm-min-f628b25083.css" />
  <!--<![endif]-->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/fzdm/st@82e930ac4ee3053246011a13e200d1fef30e110e/pure/fzdm-d8993397ea.css" />
  <!--[if IE 9]>
  <script type="text/javascript" src="https://cdn.jsdelivr.net/gh/fzdm/st@d24ab7c6533348334da08feaf462e72258d28fa7/js/pie/PIE_IE9.js"></script>
<![endif]-->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/toastr@2.1.4/build/toastr.min.css" />
  <link rel="icon" href="https://static.fzdm.com/favicon.ico" mce_href="https://static.fzdm.com/favicon.ico" type="image/x-icon" />
  <meta name="renderer" content="webkit" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <link rel="apple-touch-icon" href="https://static.fzdm.com/apple-touch-icon-144x144.png" />
  <!--[if !IE]>
  <script type="text/javascript" src="https://cdn.jsdelivr.net/gh/fzdm/st@5308a3bb0ffc8602b7d4e21afb5b71a1339af0f2/js/bc-32224ce61c.js"></script>
<!-->
  <script>if("serviceWorker"in navigator){navigator.serviceWorker.register("/sw.js",{scope:"/"}).then(function(e){var i;if(e.installing){console.log("installing")}else if(e.waiting){console.log("waiting")}else if(e.active){console.log("active")}console.log("ServiceWorker registration successful with scope: ",e.scope)})["catch"](function(e){console.log("ServiceWorker registration failed: ",e)})}</script>
  <!--<![endif]-->
  <script>if(/(iphone|ipod|ios|android|mobile)/i.test(navigator.userAgent.toLowerCase())){document.writeln("<style>");document.writeln(".logo{top: 0;}");document.writeln(".logo img {");document.writeln("width: 100%;");document.writeln("height: 100%;");document.writeln("}");document.writeln("</style>")}</script> 
  <link rel="stylesheet" href="https://static.fzdm.com/pure/mh-2bde3af992.css" />
  <script>if(/(iphone|ipod|ios|android|mobile)/i.test(navigator.userAgent.toLowerCase())){document.writeln("<style>");document.writeln("    img {");document.writeln("    width: 85%;");document.writeln("}");document.writeln("h2{font-size: 14px;}");document.writeln("#content li {");document.writeln("  line-height: 25px;");document.writeln("}");document.writeln("  .navigation {font-size: 17px;}");document.writeln("  #header{position: fixed;");document.writeln("  z-index: 1;}");document.writeln("  </style>")}else{document.writeln("<style>");document.writeln("#header{position: fixed;");document.writeln("z-index: 1;}");document.writeln("</style>")}</script> 
  <script type="text/javascript">var _hmt=_hmt||[];(function(){var e=document.createElement("script");e.src="//hm.baidu.com/hm.js?cb51090e9c10cda176f81a7fa92c3dfc";var c=document.getElementsByTagName("script")[0];c.parentNode.insertBefore(e,c)})()</script>
 </head>
 <body>
  <!--[if lt IE 9]>
<script src="https://cdn.jsdelivr.net/gh/fzdm/st@d24ab7c6533348334da08feaf462e72258d28fa7/js/html5shiv-53d12cf12b.min.js"></script>
<![endif]-->
  <script src="https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js"></script>
  <script src="https://cdn.jsdelivr.net/gh/fzdm/st@d24ab7c6533348334da08feaf462e72258d28fa7/js/fzdm-6165b8de85.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/toastr@2.1.4/toastr.min.js"></script>
  <script src="https://cdn.jsdelivr.net/gh/fzdm/st@2c55369881d0290a5e15310b1a0d2ae36f96ef93/js/u-89f900564c.js"></script> 
  <script async="" src="//dup.baidustatic.com/js/dm.js"></script>
  <div id="header">
   <div class="pure-g">
    <div class="pure-menu pure-menu-open pure-menu-horizontal">
     <div class="logo">
      <a href="//www.fzdm.com"><img src="https://static.fzdm.com/css/logo.png" alt="风之动漫" /></a>
     </div>
     <ul class="pure-menu-list">
      <li class="pure-menu-item"><a href="//www.fzdm.com/" class="pure-menu-link">首页</a></li>
      <li class="pure-menu-item"><a href="//news.fzdm.com/" class="pure-menu-link">动漫新闻</a></li>
      <li class="pure-menu-item"><a href="//manhua.fzdm.com/" class="pure-menu-link">在线漫画</a></li>
      <script>if(/(iphone|ipod|ios|android|mobile)/i.test(navigator.userAgent.toLowerCase())){}else{document.writeln("<li class='pure-menu-item'><a href='//flash.fzdm.com/' class='pure-menu-link'>动漫flash</a></li>")}</script>
     </ul>
    </div>
   </div>
  </div> 
  <script>if(/(iphone|ipod|ios|android|mobile)/i.test(navigator.userAgent.toLowerCase())){}else{}</script>
  <br /> 
  <div class="pure-g">
   <div id="content">
    <h2>七原罪漫画 七大罪七原罪在线漫画 七原罪全集</h2>
    <img src="https://static.fzdm.com/none.png" alt="七原罪漫画" />
    <br />
    <script>if(/(iphone|ipod|ios|android|mobile)/i.test(navigator.userAgent.toLowerCase())){}else{document.writeln('<div id="share" class="pure-u-md-18-24">');document.writeln('<div class="bdsharebuttonbox"><a href="#" class="bds_more" data-cmd="more">分享<strong>七原罪漫画</strong>到：</a><a href="#" class="bds_qzone" data-cmd="qzone" title="分享到QQ空间">QQ空间</a><a href="#" class="bds_weixin" data-cmd="weixin" title="分享到微信">微信</a><a href="#" class="bds_tsina" data-cmd="tsina" title="分享到新浪微博">新浪</a><a href="#" class="bds_tqq" data-cmd="tqq" title="分享到腾讯微博">腾讯</a><a href="#" class="bds_fbook" data-cmd="fbook" title="分享到Facebook">Facebook</a><a href="#" class="bds_baidu" data-cmd="baidu" title="分享到百度搜藏">百度搜藏</a><a href="#" class="bds_bdhome" data-cmd="bdhome" title="分享到百度新首页">百度首页</a></div>');document.writeln('<a href="#comment">七原罪漫画评论区</a>');document.writeln("</div>")}</script>
    <div id="mhlistad"></div> 
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="318/" title="七原罪318话">七原罪318话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="317/" title="七原罪317话">七原罪317话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="316/" title="七原罪316话">七原罪316话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="315/" title="七原罪315话">七原罪315话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="314/" title="七原罪314话">七原罪314话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="313/" title="七原罪313话">七原罪313话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="311/" title="七原罪311话">七原罪311话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="310/" title="七原罪310话">七原罪310话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="309/" title="七原罪309话">七原罪309话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="308/" title="七原罪308话">七原罪308话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="307/" title="七原罪307话">七原罪307话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="306/" title="七原罪306话">七原罪306话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="305/" title="七原罪305话">七原罪305话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="304/" title="七原罪304话">七原罪304话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="303/" title="七原罪303话">七原罪303话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="302/" title="七原罪302话">七原罪302话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="301/" title="七原罪301话">七原罪301话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="299/" title="七原罪299话">七原罪299话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="298/" title="七原罪298话">七原罪298话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="296/" title="七原罪296话">七原罪296话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="295/" title="七原罪295话">七原罪295话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="294/" title="七原罪294话">七原罪294话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="293/" title="七原罪293话">七原罪293话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="292/" title="七原罪292话">七原罪292话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="291/" title="七原罪291话">七原罪291话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="290/" title="七原罪290话">七原罪290话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="289/" title="七原罪289话">七原罪289话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="288/" title="七原罪288话">七原罪288话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="287/" title="七原罪287话">七原罪287话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="286/" title="七原罪286话">七原罪286话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="285/" title="七原罪285话">七原罪285话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="284/" title="七原罪284话">七原罪284话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="283/" title="七原罪283话">七原罪283话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="282/" title="七原罪282话">七原罪282话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="281/" title="七原罪281话">七原罪281话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="280/" title="七原罪280话">七原罪280话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="279/" title="七原罪279话">七原罪279话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="278/" title="七原罪278话">七原罪278话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="277/" title="七原罪277话">七原罪277话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="276/" title="七原罪276话">七原罪276话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="妹妹啊/" title="七原罪妹妹啊">七原罪妹妹啊</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="番外篇/" title="七原罪番外篇">七原罪番外篇</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="275/" title="七原罪275话">七原罪275话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="274/" title="七原罪274话">七原罪274话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="273/" title="七原罪273话">七原罪273话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="272/" title="七原罪272话">七原罪272话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="271/" title="七原罪271话">七原罪271话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="270/" title="七原罪270话">七原罪270话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="269/" title="七原罪269话">七原罪269话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="268/" title="七原罪268话">七原罪268话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="266/" title="七原罪266话">七原罪266话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="265/" title="七原罪265话">七原罪265话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="264/" title="七原罪264话">七原罪264话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="263/" title="七原罪263话">七原罪263话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="262/" title="七原罪262话">七原罪262话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="261/" title="七原罪261话">七原罪261话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="260/" title="七原罪260话">七原罪260话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="259/" title="七原罪259话">七原罪259话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="258/" title="七原罪258话">七原罪258话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="257/" title="七原罪257话">七原罪257话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="256/" title="七原罪256话">七原罪256话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="255/" title="七原罪255话">七原罪255话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="254/" title="七原罪254话">七原罪254话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="253/" title="七原罪253话">七原罪253话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="252/" title="七原罪252话">七原罪252话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="251/" title="七原罪251话">七原罪251话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="250/" title="七原罪250话">七原罪250话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="249/" title="七原罪249话">七原罪249话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="248/" title="七原罪248话">七原罪248话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="247/" title="七原罪247话">七原罪247话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="245/" title="七原罪245话">七原罪245话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="244/" title="七原罪244话">七原罪244话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="243/" title="七原罪243话">七原罪243话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="242/" title="七原罪242话">七原罪242话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="241/" title="七原罪241话">七原罪241话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="240/" title="七原罪240话">七原罪240话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="239/" title="七原罪239话">七原罪239话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="238/" title="七原罪238话">七原罪238话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="237/" title="七原罪237话">七原罪237话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="236/" title="七原罪236话">七原罪236话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="235/" title="七原罪235话">七原罪235话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="234/" title="七原罪234话">七原罪234话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="233/" title="七原罪233话">七原罪233话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="232/" title="七原罪232话">七原罪232话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="231/" title="七原罪231话">七原罪231话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="230/" title="七原罪230话">七原罪230话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="229/" title="七原罪229话">七原罪229话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="228/" title="七原罪228话">七原罪228话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="227/" title="七原罪227话">七原罪227话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="223/" title="七原罪223话">七原罪223话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="222/" title="七原罪222话">七原罪222话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="221/" title="七原罪221话">七原罪221话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="226/" title="七原罪226话">七原罪226话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="225/" title="七原罪225话">七原罪225话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="224/" title="七原罪224话">七原罪224话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="220/" title="七原罪220话">七原罪220话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="219/" title="七原罪219话">七原罪219话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="218/" title="七原罪218话">七原罪218话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="217/" title="七原罪217话">七原罪217话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="216/" title="七原罪216话">七原罪216话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="215/" title="七原罪215话">七原罪215话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="214/" title="七原罪214话">七原罪214话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="213/" title="七原罪213话">七原罪213话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="212/" title="七原罪212话">七原罪212话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="roqqaq/" title="七原罪人偶祈求爱情">七原罪人偶祈求爱情</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="211/" title="七原罪211话">七原罪211话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="210/" title="七原罪210话">七原罪210话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="209/" title="七原罪209话">七原罪209话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="208/" title="七原罪208话">七原罪208话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="207/" title="七原罪207话">七原罪207话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="206/" title="七原罪206话">七原罪206话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="205/" title="七原罪205话">七原罪205话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="204/" title="七原罪204话">七原罪204话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="203/" title="七原罪203话">七原罪203话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="202/" title="七原罪202话">七原罪202话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="sp22/" title="七原罪新猪帽子亭">七原罪新猪帽子亭</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="xcdgn/" title="七原罪想传达给你">七原罪想传达给你</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="jcmfff/" title="七原罪解除魔法方法">七原罪解除魔法方法</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="201/" title="七原罪201话">七原罪201话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="200/" title="七原罪200话">七原罪200话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="199/" title="七原罪199话">七原罪199话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="198/" title="七原罪198话">七原罪198话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="197/" title="七原罪197话">七原罪197话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="196/" title="七原罪196话">七原罪196话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="195/" title="七原罪195话">七原罪195话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="194/" title="七原罪194话">七原罪194话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="193/" title="七原罪193话">七原罪193话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="192/" title="七原罪192话">七原罪192话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="191/" title="七原罪191话">七原罪191话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="190/" title="七原罪190话">七原罪190话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="189/" title="七原罪189话">七原罪189话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="188/" title="七原罪188话">七原罪188话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="187/" title="七原罪187话">七原罪187话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="186/" title="七原罪186话">七原罪186话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="185/" title="七原罪185话">七原罪185话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="184/" title="七原罪184话">七原罪184话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="183/" title="七原罪183话">七原罪183话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="182/" title="七原罪182话">七原罪182话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="181/" title="七原罪181话">七原罪181话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="180/" title="七原罪180话">七原罪180话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="179/" title="七原罪179话">七原罪179话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="178/" title="七原罪178话">七原罪178话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="177/" title="七原罪177话">七原罪177话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="176/" title="七原罪176话">七原罪176话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="175/" title="七原罪175话">七原罪175话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="174/" title="七原罪174话">七原罪174话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="173/" title="七原罪173话">七原罪173话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="172/" title="七原罪172话">七原罪172话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="171/" title="七原罪171话">七原罪171话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="170/" title="七原罪170话">七原罪170话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="169/" title="七原罪169话">七原罪169话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="168/" title="七原罪168话">七原罪168话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="167/" title="七原罪167话">七原罪167话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="166/" title="七原罪166话">七原罪166话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="165/" title="七原罪165话">七原罪165话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="164/" title="七原罪164话">七原罪164话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="163/" title="七原罪163话">七原罪163话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="162/" title="七原罪162话">七原罪162话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="161/" title="七原罪161话">七原罪161话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="160/" title="七原罪160话">七原罪160话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="159/" title="七原罪159话">七原罪159话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="158/" title="七原罪158话">七原罪158话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="157/" title="七原罪157话">七原罪157话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="156/" title="七原罪156话">七原罪156话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="155/" title="七原罪155话">七原罪155话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="154/" title="七原罪154话">七原罪154话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="153/" title="七原罪153话">七原罪153话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="152/" title="七原罪第152话">七原罪第152话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="150/" title="七原罪第150话">七原罪第150话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="149/" title="七原罪第149话">七原罪第149话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="148/" title="七原罪148话">七原罪148话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="147/" title="七原罪147话">七原罪147话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="146/" title="七原罪146话">七原罪146话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="sp19/" title="七原罪赤裸的心">七原罪赤裸的心</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="145/" title="七原罪145话">七原罪145话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="144/" title="七原罪144话">七原罪144话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="143/" title="七原罪143话">七原罪143话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="142/" title="七原罪142话">七原罪142话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="141/" title="七原罪141话">七原罪141话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="140/" title="七原罪140话">七原罪140话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="139/" title="七原罪139话">七原罪139话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="138/" title="七原罪138话">七原罪138话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="137/" title="七原罪137话">七原罪137话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="136/" title="七原罪136话">七原罪136话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="xxgxp/" title="七原罪吸血鬼下篇">七原罪吸血鬼下篇</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="xxgsp/" title="七原罪吸血鬼上篇">七原罪吸血鬼上篇</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="135/" title="七原罪135话">七原罪135话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="134/" title="七原罪134话">七原罪134话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="133/" title="七原罪133话">七原罪133话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="132/" title="七原罪132话">七原罪132话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="131/" title="七原罪131话">七原罪131话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="130/" title="七原罪130话">七原罪130话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="129/" title="七原罪129话">七原罪129话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="128/" title="七原罪128话">七原罪128话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="127/" title="七原罪127话">七原罪127话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="fwp15/" title="七原罪番外篇15">七原罪番外篇15</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="fwp14/" title="七原罪番外篇14">七原罪番外篇14</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="126/" title="七原罪126话">七原罪126话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="125/" title="七原罪125话">七原罪125话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="124/" title="七原罪124话">七原罪124话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="123/" title="七原罪123话">七原罪123话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="122/" title="七原罪122话">七原罪122话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="120/" title="七原罪120话">七原罪120话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="119/" title="七原罪119话">七原罪119话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="fwp13/" title="七原罪番外篇13">七原罪番外篇13</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="118/" title="七原罪118话">七原罪118话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="117/" title="七原罪117话">七原罪117话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="yxl/" title="七原罪有心论">七原罪有心论</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="116/" title="七原罪116话">七原罪116话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="xy12/" title="七原罪学园12">七原罪学园12</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="xy11/" title="七原罪学园11">七原罪学园11</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="115/" title="七原罪115话">七原罪115话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="114/" title="七原罪114话">七原罪114话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="113/" title="七原罪113话">七原罪113话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="112/" title="七原罪112话">七原罪112话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="111/" title="七原罪111话">七原罪111话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="110/" title="七原罪110话">七原罪110话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="109/" title="七原罪109话">七原罪109话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="108/" title="七原罪108话">七原罪108话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="107/" title="七原罪107话">七原罪107话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="106/" title="七原罪106话">七原罪106话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="105/" title="七原罪105话">七原罪105话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="104/" title="七原罪104话">七原罪104话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="103/" title="七原罪103话">七原罪103话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="102/" title="七原罪102话">七原罪102话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="100/" title="七原罪100话">七原罪100话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="99/" title="七原罪99话">七原罪99话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="98/" title="七原罪98话">七原罪98话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="97/" title="七原罪97话">七原罪97话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="96/" title="七原罪96话">七原罪96话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="95/" title="七原罪95话">七原罪95话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="94/" title="七原罪94话">七原罪94话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="93/" title="七原罪93话">七原罪93话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="92/" title="七原罪92话">七原罪92话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="91/" title="七原罪91话">七原罪91话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="90/" title="七原罪90话">七原罪90话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="89/" title="七原罪89话">七原罪89话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="88/" title="七原罪88话">七原罪88话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="87/" title="七原罪87话">七原罪87话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="86/" title="七原罪86话">七原罪86话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="85/" title="七原罪85话">七原罪85话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="84/" title="七原罪84话">七原罪84话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="fwp9/" title="七原罪番外篇9">七原罪番外篇9</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="83/" title="七原罪83话">七原罪83话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="fwp8/" title="七原罪番外篇8">七原罪番外篇8</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="82/" title="七原罪82话">七原罪82话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="81/" title="七原罪81话">七原罪81话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="80/" title="七原罪80话">七原罪80话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="79/" title="七原罪79话">七原罪79话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="77/" title="七原罪77话">七原罪77话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="76/" title="七原罪76话">七原罪76话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="75/" title="七原罪75话">七原罪75话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="74/" title="七原罪74话">七原罪74话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="wc/" title="七原罪外传">七原罪外传</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="73/" title="七原罪73话">七原罪73话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="72/" title="七原罪72话">七原罪72话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="71/" title="七原罪71话">七原罪71话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="70/" title="七原罪70话">七原罪70话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="69/" title="七原罪69话">七原罪69话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="fwp5/" title="七原罪番外篇5">七原罪番外篇5</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="68/" title="七原罪68话">七原罪68话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="fwp4/" title="七原罪番外篇4">七原罪番外篇4</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="67/" title="七原罪67话">七原罪67话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="66/" title="七原罪66话">七原罪66话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="65/" title="七原罪65话">七原罪65话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="64/" title="七原罪64话">七原罪64话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="63/" title="七原罪63话">七原罪63话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="62/" title="七原罪62话">七原罪62话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="61/" title="七原罪61话">七原罪61话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="60/" title="七原罪60话">七原罪60话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="59/" title="七原罪59话">七原罪59话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="58/" title="七原罪58话">七原罪58话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="57/" title="七原罪57话">七原罪57话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="56/" title="七原罪56话">七原罪56话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="55/" title="七原罪55话">七原罪55话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="54/" title="七原罪54话">七原罪54话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="53/" title="七原罪53话">七原罪53话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="52/" title="七原罪52话">七原罪52话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="51/" title="七原罪51话">七原罪51话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="50/" title="七原罪50话">七原罪50话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="49/" title="七原罪49话">七原罪49话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="48/" title="七原罪48话">七原罪48话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="47/" title="七原罪47话">七原罪47话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="46/" title="七原罪46话">七原罪46话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="45/" title="七原罪45话">七原罪45话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="fwp3/" title="七原罪番外篇3">七原罪番外篇3</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="44/" title="七原罪44话">七原罪44话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="43/" title="七原罪43话">七原罪43话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="42/" title="七原罪42话">七原罪42话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="41/" title="七原罪41话">七原罪41话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="40/" title="七原罪40话">七原罪40话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="39/" title="七原罪39话">七原罪39话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="38/" title="七原罪38话">七原罪38话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="37/" title="七原罪37话">七原罪37话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="36/" title="七原罪36话">七原罪36话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="35/" title="七原罪35话">七原罪35话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="34/" title="七原罪34话">七原罪34话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="33/" title="七原罪33话">七原罪33话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="32/" title="七原罪32话">七原罪32话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="tbp/" title="七原罪特别篇">七原罪特别篇</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="31/" title="七原罪31话">七原罪31话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="30/" title="七原罪30话">七原罪30话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="29/" title="七原罪29话">七原罪29话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="sdj1/" title="七原罪设定集1">七原罪设定集1</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="28/" title="七原罪28话">七原罪28话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="27/" title="七原罪27话">七原罪27话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="026/" title="七原罪026话">七原罪026话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="wzdzc/" title="七原罪外传盗贼梵">七原罪外传盗贼梵</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="025/" title="七原罪025话">七原罪025话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="024/" title="七原罪024话">七原罪024话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="023/" title="七原罪023话">七原罪023话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="022/" title="七原罪022话">七原罪022话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="021/" title="七原罪021话">七原罪021话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="020/" title="七原罪020话">七原罪020话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="019/" title="七原罪019话">七原罪019话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="018/" title="七原罪018话">七原罪018话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="017/" title="七原罪017话">七原罪017话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="016/" title="七原罪016话">七原罪016话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="015/" title="七原罪015话">七原罪015话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="014/" title="七原罪014话">七原罪014话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="013/" title="七原罪013话">七原罪013话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="012/" title="七原罪012话">七原罪012话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="011/" title="七原罪011话">七原罪011话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="010/" title="七原罪010话">七原罪010话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="009/" title="七原罪009话">七原罪009话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="008/" title="七原罪008话">七原罪008话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="007/" title="七原罪007话">七原罪007话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="006/" title="七原罪006话">七原罪006话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="005/" title="七原罪005话">七原罪005话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="004/" title="七原罪004话">七原罪004话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="003/" title="七原罪003话">七原罪003话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="002/" title="七原罪002话">七原罪002话</a></li>
    <li class="pure-u-1-2 pure-u-lg-1-4"><a href="001/" title="七原罪001话">七原罪001话</a></li> 
   </div>
   <br />
   <div id="content"></div>
  </div>
  <script>window._bd_share_config={common:{bdSnsKey:{},bdText:"七原罪漫画 风之动漫",bdDesc:"推荐：看七原罪漫画的好网站 风之动漫",bdMini:"2",bdMiniList:false,bdSign:"",bdPic:"",bdStyle:"0",bdSize:"16"},share:{bdSize:16}};with(document)(0)[(getElementsByTagName("head")[0]||body).appendChild(createElement("script")).src="https://cdn.jsdelivr.net/gh/fzdm/st@4a86505ed279869679b8ef509df7a88326f642c8/js/share-26b16ca544.js?v=89860593.js?cdnversion="+~(-new Date/36e5)]</script> 
  <div class="clear"></div>
  <div id="footer">
   <div id="hd">
    <div class="bg"></div>
    <br />
    <a href="//www.fzdm.com/about">关于我们</a> | 
    <a href="//www.fzdm.com/lianxi">联系我们</a> | 
    <a href="//www.fzdm.com/map">网站地图</a>
    <br />Copyright ⓒ 2014-2015 风之动漫 版本beta 0.4
    <br />
   </div>
  </div> 
  <script>if(/(iphone|ipod|ios|android|mobile)/i.test(navigator.userAgent.toLowerCase())){document.writeln("")}else{document.writeln("<script src='https://jy.ggweb.net/fzfmt.js'><\/script>")}</script> 
  <div id="speed"></div>
  <script>testing()</script>
 </body>
</html>
''' 
html = etree.HTML(html)


ele = html.xpath('//*[@id="content"]//li//a//@href') # urls
print(ele)
print(len(ele))
    # 
    # for u in urls:
                    
    #     print("this page urls is " + u)
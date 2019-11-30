pageString = '''








<!--  global include -->

	
	
	
	
	
<html lang='ko'>
<head>


	
	
		
			
			
				<title>시가총액 : 네이버 금융</title>
			
		
	





	
	
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	


<meta http-equiv="Content-Script-Type" content="text/javascript">
<meta http-equiv="Content-Style-Type" content="text/css">




	
    
        <meta property="og:url" content="http://finance.naver.com/sise/sise_market_sum.nhn"/>
        
			
		    
		    	<meta property="og:title" content="시가총액 : 네이버 금융"/>
		     
		
		
			
			   <meta property="og:description" content="관심종목의 실시간 주가를 가장 빠르게 확인하는 곳"/>
		    
		    
		
		 
			
			    <meta property="og:image" content="https://ssl.pstatic.net/static/m/stock/im/2016/08/og_stock-200.png"/>
		    
		    
		
    

<meta property="og:type" content="article"/>
<meta property="og:article:thumbnailUrl" content=""/>
<meta property="og:article:author" content="네이버금융"/>
<meta property="og:article:author:url" content="http://FINANCE.NAVER.COM"/>




<link rel='stylesheet' type='text/css' href='/css/finance_header.css?20191114133508'>

	
	
	
	
		<link rel="stylesheet" type="text/css" href="/css/newstock.css?20191114133508">
		<link rel="stylesheet" type="text/css" href="/css/common.css?20191114133508">
		<link rel="stylesheet" type="text/css" href="/css/layout.css?20191114133508">
		<link rel="stylesheet" type="text/css" href="/css/main.css?20191114133508">
		<link rel="stylesheet" type="text/css" href="/css/newstock2.css?20191114133508">
		<link rel="stylesheet" type="text/css" href="/css/newstock3.css?20191114133508">
		<link rel="stylesheet" type="text/css" href="/css/world.css?20191114133508">
		
		
		
		

		
		
		
			<script type="text/javascript" src="/js/jindo.min.ns.1.5.3.euckr.js?20191114133508"></script>
			
			
				<script type="text/javascript" src="/js/release/common.js?20191114133508"></script>
			
		
			<script type="text/javascript" src="/js/jindoComponent/jindo.Component.1.0.3.js?20191114133508"></script>
			<script type="text/javascript" src="/ac/nhn.autocomplete.stock.js?20191114133508"></script>
		
		
	


	<link rel="shortcut icon" href="https://www.naver.com/favicon.ico?20191114133508" type="image/x-icon">
	
	<script type="text/javascript">
    (function(){
        var sUserAgent = navigator.userAgent;
        if(/iPhone|iPad/.test(sUserAgent)){
            document.write(
                [
					'<link rel="apple-touch-icon-precomposed" sizes="120x120" href="https://ssl.pstatic.net/static/nfinance/ico/2018_ios_120X120_iphone.png" />',
					'<link rel="apple-touch-icon-precomposed" sizes="152x152" href="https://ssl.pstatic.net/static/nfinance/ico/2018_ios_152x152_ipad.png" />',
					'<link rel="apple-touch-icon-precomposed" sizes="167x167" href="https://ssl.pstatic.net/static/nfinance/ico/2018_ios_167x167_ipad_pro.png" />',
					'<link rel="apple-touch-icon-precomposed" sizes="180x180" href="https://ssl.pstatic.net/static/nfinance/ico/2018_ios_180x180_iphone.png" />'
                ]
                .join('\n')
            );
        }

        if(/Android/.test(sUserAgent)){
            document.write(
                [
                    '<link rel="apple-touch-icon-precomposed" sizes="72x72" href="https://ssl.pstatic.net/static/nfinance/ico/2018_android_72x72_xxxhpdi.png" />',
                    '<link rel="apple-touch-icon-precomposed" sizes="96x96" href="https://ssl.pstatic.net/static/nfinance/ico/2018_android_96x96_xxxhpdi.png" />',
                    '<link rel="apple-touch-icon-precomposed" sizes="144x144" href="https://ssl.pstatic.net/static/nfinance/ico/2018_android_144x144_xxxhpdi.png" />',
                    '<link rel="apple-touch-icon-precomposed" sizes="192x192" href="https://ssl.pstatic.net/static/nfinance/ico/2018_android_192x192_xxxhpdi.png" />'
				]
				.join('\n')
			);
        }
    })();
    </script>
</head>




<body onload='getGNB();'>



<script type="text/javascript">
	document.domain = 'naver.com';
	var nclk_evt = 3;
	nclk_do();
</script>


<script type="text/javascript">




var nsc="finance.stock";





var ccsrv="cc.naver.com";


	
	
	var gnb_service='finance';
	


var gnb_logout=document.URL; //GNB에서 로그아웃 후 redirect 될 URL
var gnb_searchbox='off'; //미니 검색창을 on 할지 off 할지. default는 off
var gnb_shortnick='off'; //닉네임 말줄임(10자)을 on할지 off 할지. default는 off.


var gnb_naverme_layer_open_callback = function(){
	   var naverLayerSize = gnbNaverMeLayer.getLayerSize();
		
		var me_layers = document.getElementById("me_layers");
		me_layers.width=naverLayerSize.width;
		me_layers.height=naverLayerSize.height;};

var gnb_naverme_layer_close_callback = function(){
		
			var me_layers = document.getElementById("me_layers");
			me_layers.width="0";
			me_layers.height="0";};
</script>


<div id="u_skip">
	<a href="#menu" tabindex="1"><span>메인 메뉴로 바로가기</span></a>

	
	
		<a href="#start" tabindex="2"><span>본문으로 바로가기</span></a>
	

</div>


<div id="header">
	<div class="snb_area">
		<div class="snb_inner">
			<div id="gnb_area">
				<div id="gnb">
					<script charset="EUC-KR" type="text/javascript">
					var gnb_service = "gnbtest";
                    var gnb_template = location.protocol == "http:" ? "gnb_quirks_euckr" : "gnb_utf8" ;
					var gnb_dark = false;
					var gnb_brightness = 1;
					var gnb_logout=encodeURIComponent(location.href);
					var gnb_one_naver = 1;
					</script>
					
						
						
							<script type="text/javascript" charset="utf-8" src="https://ssl.pstatic.net/static.gn/templates/gnb_utf8.nhn?20191130">
                    		</script>
						
					
				</div>
			</div>

			<div class="sta">
				<h1 class="logo"> <a href="https://www.naver.com/" class="logo_naver" onClick="clickcr(this, 'STA.naver', '', '', event);"><span class="blind">네이버</span></a>
				<a href="/" class="logo_service" onClick="clickcr(this, 'STA.finance', '', '', event);"><span class="blind">금융</span></a> </h1>
				<form name="search" action="/search/search.nhn"  method="get"
					onsubmit="return delayed_submit(this)" style="margin:0; padding:0;">
				<fieldset>
					<legend>검색</legend>
					<div class="snb_search_box">
						<div class="snb_search_box_sub">
							<input id="stock_items" type="text" title="검색" name="query" value="종목명&middot;펀드명&middot;환율명&middot;원자재명 입력" accesskey="s" class="snb_search_text snb_default" autocomplete="off">
							<a id="nautocomplete" href="#" onclick="return false" class="btn_arrow"><span class="blind">자동완성 펼치기</span></a>
						</div>
						<div class="auto_area">
							<h2 class="blind">자동완성</h2>
							<iframe id="autoFrame" src="/ac/reatcmp.nhn?menu=sise&submenu=" scrolling="no" height="0" frameborder="0" width="400" style="display: none;" marginheight="0" marginwidth="0" title="자동완성"></iframe>
						</div>
						<button type="submit" class="snb_search_btn" onclick="clickcr(this, 'STA.search', '', '', event);" alt="검색"><span class="blind">검색</span></button>
						<a href="#" target="_blank" class="snb_search_btn-total" onclick="itegrationSearch();clickcr(this, 'STA.nx', '', '', event);return false;">통합검색</a>
					</div>
				</fieldset>
				</form>
			</div>
		</div>
	</div>
	<div class="lnb_area ">
		<div class="lnb_inner">
			<div id="menu">
				<ul class="menu">
					<li class="m1 first "><a href="/" onClick="clickcr(this, 'LNB.home', '', '', event);"><span class="tx">금융 홈</span></a></li>
					<li class="m2 on"><a href="/sise/" onClick="clickcr(this, 'LNB.sise', '', '', event);"><span class="tx">국내증시</span></a></li>
					<li class="m3 "><a href="/world/" onClick="clickcr(this, 'LNB.world', '', '', event);"><span class="tx">해외증시</span></a></li>
					<li class="m4 "><a href="/marketindex/" onClick="clickcr(this, 'LNB.market', '', '', event);"><span class="tx">시장지표</span></a></li>
					<li class="m5 "><a href="/fund/" onClick="clickcr(this, 'LNB.fund', '', '', event);"><span class="tx">펀드</span></a>
						
					</li>
					<li class="m6 "><a href="/research/" onClick="clickcr(this, 'LNB.research', '', '', event);"><span class="tx">투자전략</span></a></li>
					<li class="m7 "><a href="/news/"><span class="tx">뉴스</span></a></li>
					<li class="m8 "><a href="/mystock/" onClick="clickcr(this, 'LNB.mystock', '', '', event);"><span class="tx">MY</span></a></li>
				</ul>
			</div>
		</div>
	</div>
	
	
	
	

	
	<script type="text/JavaScript">
		/* lcs 집계 */
        ;(function(){
            var eventType = "onpageshow" in window ? "pageshow" : "load";
            jindo.$Fn(function(){
                lcs_do();
            }).attach(window, eventType);
        })();

		/* 검색 자동완성 [ 인자1 : 검색input의 ID, 인자2 : iframe 태그 ID ]   */
		// AutoComplete 생성
		var acDomain = "ac.finance.naver.com";
        if (location.hostname.indexOf("staging-") > -1) {
            acDomain = "staging-" + acDomain;
        }
        var acUrl = "https://" + acDomain + "/ac";

		smartSearch = new nhn.Autocomplete(
			// InputManager 생성
			new nhn.AcInputManager(jindo.$("stock_items")),
			// DataManager 생성
			new nhn.AcDataManager(acUrl, "jsonp", "get", {
                    st: "111",
                    r_lt : "111",
                    q_enc : "euc-kr",
                    r_enc : "euc-kr",
                    frm: "stock"}),
			// ViewManager 생성
			new nhn.AcStockViewManager(jindo.$("autoFrame"), jindo.$("nautocomplete"), {
                                        strMax: 200,
                                        listMax: [7, 2, 2],
                                        aRedirectUrl : [
                            			"https://finance.naver.com",
                            			"https://finance.naver.com",
                            			"https://finance.naver.com"]}),
			// Autocomplete Option
            {formId:"search", cookieDomain:location.hostname, cookieName:"NaverCommonStock"});

			smartSearch.attach({
	            onFocus: function () {
	                var weInput = jindo.$Element('stock_items');
	                if (weInput && weInput.hasClass("snb_default")) {
	                        weInput.text("");
	                        weInput.removeClass('snb_default');
	                }
	            }
	        });

		/* 통합검색  start ----->  */
		document.domain = 'naver.com';
		var sSearchHintText = '종목명·펀드명·환율명·원자재명 입력';
		function itegrationSearch() {
			var query = jindo.$('stock_items').value;

			if ( query == ''  || encodeURIComponent(query) == encodeURIComponent(sSearchHintText))
			{
				alert ( '검색어를 입력해 주세요.' );
				return;
			}

            var url = location.protocol + "//search.naver.com/search.naver?sm=sta_hty.finance&where=nexearch&ie=UTF8&query=" + encodeURIComponent(query);
            window.open(url, "_blank");

			return false;
		}

		function delayed_submit(object) {
			if (navigator.userAgent.indexOf('MSIE') == -1) {
				window.setTimeout(function() {stock_search(object)}, 300);
			} else {
				stock_search(object);
			}
			return false;
		}

		function stock_search (object)
		{
			query = object.query.value.replace(/^\s*/,'').replace(/\s*$/,'');	// trim
			object.query.value=query;

			if ( query == '' || query == sSearchHintText.replace(/^\s*/,'').replace(/\s*$/,''))
			{
				alert ( '검색어를 입력해 주세요.' );
				return;
			}
			else {
				object.submit();
			}
		}
		/* <---------- 통합검색  end */

		function popup()
		{
			win = window.open('/template/group_limit_pop.jsp','finan_popup','width=569 height=278 scrollbars=no status=no');
			win.focus();
		}
	</script>

	<iframe id="me_layers" name="test" title="네이버미 영역" width="0" height="0" scrolling="no" frameborder="0" style="display:block;top: 22px; right: 209px; position: absolute; z-index: 15;"></iframe>
</div>
<div id="wrap"  >

<!-- //  global include -->
<script language="JavaScript">
function mouseOver(obj){
  obj.style.backgroundColor="#f6f4e5";
}
function mouseOut(obj){
  obj.style.backgroundColor="#ffffff";
}
</script>

	<div id="newarea">
			

			<!-- leftmenu -->
			<div class="snb snb2">
				<h2 class="h_sise"><a href="/sise/"><span class="blind">국내증시</span></a></h2>
				<ul class="nav1">
				<li class="frst"><strong class="lst_sise"><span class="blind">주요시세정보</span></strong>
					<ul class="sub">
					 <li class="type1 lst1_1"><a href="/sise/sise_index.nhn?code=KOSPI" onClick="clickcr(this,'siu.1','','',event);" class="off"><span class="blind">코스피</span></a></li> 
                     <li class="type1 lst1_2"><a href="/sise/sise_index.nhn?code=KOSDAQ" onClick="clickcr(this,'siu.2','','',event);" class="off"><span class="blind">코스닥</span></a></li>
                     <li class="type1 lst1_3"><a href="/sise/sise_index.nhn?code=FUT" onClick="clickcr(this,'siu.3','','',event);" class="off"><span class="blind">선물</span></a></li>
                     <li class="type1 lst1_26"><a href="/sise/sise_index.nhn?code=KPI200" onClick="clickcr(this,'siu.26','','',event);" class="off"><span class="blind">코스피200</span></a></li>
                     <li class="type1 lst1_31"><a href="/sise/konex.nhn" onClick="clickcr(this,'siu.konex','','',event);" class="off"><span class="blind">코넥스</span></a></li>
                     <li class="type1 lst1_16"><a href="/sise/sise_market_sum.nhn" onClick="clickcr(this,'siu.16','','',event);" class="on"><span class="blind">시가총액</span></a></li>
                     <li class="type1 lst1_32" ><a href="/sise/dividend_list.nhn" onClick="clickcr(this,'siu.dividend','','',event);" class="off"><span class="blind">배당</span></a></li>                     
                     <li class="type1 lst1_4"><a href="/sise/sise_group.nhn?type=upjong" onClick="clickcr(this,'siu.4','','',event);" class="off"><span class="blind">업종</span></a></li>
                     <li class="type1 lst1_5" ><a href="/sise/theme.nhn" onClick="clickcr(this,'siu.5','','',event);" class="off"><span class="blind">테마</span></a></li>
                     <li class="type1 lst1_30"><a href="/sise/sise_group.nhn?type=group"  onClick="clickcr(this,'siu.30','','',event);"  class="off"><span class="blind">그룹사</span></a></li>
					 <li class="type1 lst1_27 "><a href="/sise/etf.nhn" onClick="clickcr(this,'siu.27','','',event);" class="off"><span class="blind">ETF</span></a></li>
					 <li class="type1 lst1_34"><a href="/sise/etn.nhn" onClick="clickcr(this,'siu.34','','',event);" class="off"><span class="blind">ETN</span></a></li>
					 <li class="type1 lst1_8 "><a href="/sise/sise_rise.nhn" onClick="clickcr(this,'siu.8','','',event);" class="off"><span class="blind">ª?Ω?</span></a></li>
                     <li class="type1 lst1_9 "><a href="/sise/sise_steady.nhn" onClick="clickcr(this,'siu.9','','',event);" class="off"><span class="blind">보합</span></a></li>
                     <li class="type1 lst1_10"><a href="/sise/sise_fall.nhn" onClick="clickcr(this,'siu.10','','',event);" class="off"><span class="blind">하락</span></a></li>
                     <li class="type1 lst1_6"><a href="/sise/sise_upper.nhn" onClick="clickcr(this,'siu.6','','',event);" class="off"><span class="blind">상한가</span></a></li>
                     <li class="type1 lst1_7"><a href="/sise/sise_lower.nhn" onClick="clickcr(this,'siu.7','','',event);" class="off"><span class="blind">하한가</span></a></li>
                     <li class="type1 lst1_15 "><a href="/sise/sise_low_up.nhn" onClick="clickcr(this,'siu.15','','',event);" class="off"><span class="blind">급등</span></a></li>
                     <li class="type1 lst1_14 "><a href="/sise/sise_high_down.nhn" onClick="clickcr(this,'siu.14','','',event);" class="off"><span class="blind">급락</span></a></li>
                     <li class="type2 lst1_11"><a href="/sise/sise_quant.nhn" onClick="clickcr(this,'siu.11','','',event);" class="off"><span class="blind">거래상위</span></a></li>  
                     <li class="type1 lst1_12 "><a href="/sise/sise_quant_high.nhn" onClick="clickcr(this,'siu.12','','',event);" class="off"><span class="blind">급증</span></a></li> 
                     <li class="type1 lst1_13 "><a href="/sise/sise_quant_low.nhn" onClick="clickcr(this,'siu.13','','',event);" class="off"><span class="blind">급감</span></a></li>
                     <li class="lst1_23"><a href="/sise/sise_trans_style.nhn" onClick="clickcr(this,'siu.23','','',event);" class="off"><span class="blind">투자자별매매동향</span></a></li>  
                     <li class="type1 lst1_17"><a href="/sise/sise_deal_rank.nhn" onClick="clickcr(this,'siu.17','','',event);" class="off"><span class="blind">외국인매매</span></a></li> 
                     <li class="type1 lst1_18"><a href="/sise/sise_deal_rank.nhn?investor_gubun=1000" onClick="clickcr(this,'siu.18','','',event);" class="off"><span class="blind">기관매매</span></a></li> 
                     <li class="lst1_19"><a href="/sise/sise_program.nhn" onClick="clickcr(this,'siu.19','','',event);" class="off"><span class="blind">프로그램매매동향</span></a></li> 
                     <li class="lst1_22"><a href="/sise/sise_deposit.nhn" onClick="clickcr(this,'siu.22','','',event);" class="off"><span class="blind">증시자금동향</span></a></li>
                     <li class="lst1_21"><a href="/sise/sise_new_stock.nhn" onClick="clickcr(this,'siu.21','','',event);" class="off"><span class="blind">신규상장</span></a></li>  
                     <li class="lst1_24 "><a href="/sise/sise_foreign_hold.nhn" onClick="clickcr(this,'siu.24','','',event);" class="off"><span class="blind">외국인보유</span></a></li> 
                     <li class="lst1_25 "><a href="/sise/market3news_list.nhn" onClick="clickcr(this,'siu.25','','',event);" class="off"><span class="blind">장외시세</span></a></li>
                     <li class="lst1_33 "><a href="/sise/ipo.nhn" onClick="clickcr(this,'siu.33','','',event);" class="off"><span class="blind">IPO</span></a></li>
					</ul>
				</li>
				<li><strong class="lst_prevent"><span class="blind">투자자보호</span></strong>
	                <ul class="sub">
	                 <li class="lst1_20"><a href="/sise/management.nhn" onClick="clickcr(this,'siu.20','','',event);" class="off"><span class="blind">관리종목</span></a></li>
	                 <li class="lst1_29"><a href="/sise/trading_halt.nhn" onClick="clickcr(this,'siu.29','','',event);" class="off"><span class="blind">거래정지종목</span></a></li> 
	                 <li class="lst1_28"><a href="/sise/investment_alert.nhn?type=caution" onClick="clickcr(this,'siu.28','','',event);" class="off"><span class="blind">시장경보종목</span></a></li>
	                </ul>
            	</li>
    			<li><strong class="lst_search"><span class="blind">종목조건검색</span></strong>
					<ul class="sub">
					 <li class="type1 lst2_2"><a href="/sise/item_gold.nhn" onClick="clickcr(this,'sih.2','','',event);" class="off"><span class="blind">골든크로스</span></a></li>
					 <li class="type1 lst2_1"><a href="/sise/item_gap.nhn" onClick="clickcr(this,'sih.1','','',event);" class="off"><span class="blind">갭상승</span></a></li>
					 <li class="type1 lst2_3"><a href="/sise/item_igyuk.nhn" onClick="clickcr(this,'sih.3','','',event);" class="off"><span class="blind">이격도과열</span></a></li>
					 <li class="type1 lst2_4"><a href="/sise/item_overheating_1.nhn" onClick="clickcr(this,'sih.4','','',event);" class="off"><span class="blind">투심과열</span></a></li>
					 <li class="lst2_5"><a href="/sise/item_overheating_2.nhn" onClick="clickcr(this,'sih.5','','',event);" class="off"><span class="blind">상대강도과열</span></a></li>  	                 
					</ul>
				</li>
				<li><a href="/sise/report.nhn"><strong class="lst_report"><span class="blind">기업 전자공시</span></strong></a></li>
				<li class="last"><a href="/sise/short_trade.nhn"><strong class="lst_short"><span class="blind">공매도 종합 현황</span></strong></a></li>				
				</ul>
								
			</div>
			<!-- //leftmenu -->
			
			<!-- //leftmenu -->
		<div id="contentarea">
			<!-- 컨텐츠 -->
			<div id="contentarea_left" class="bnd_wid">
				<!-- 로케이터 : 메뉴에 맞게 고쳐주세요 -->
				<div class="sub_location tlt_bottom_line">
					<a href="/">금융홈</a> &gt; <a href="/sise/">국내증시</a> &gt; <a href="#">시가총액</a>
				</div>
				<!-- //로케이터 -->

				<h3 class="sub_tlt">시가총액<span class="tlt_page">항목을 자유롭게 변경하실 수 있습니다.&nbsp;&nbsp;<img src='https://ssl.pstatic.net/imgstock/images5/bar_C7C.gif'>&nbsp;&nbsp;최대 6개까지 설정 가능합니다.</span></h3>
			<!-- 항목선택 -->
		
		
	


 
 
 	
 	
 


<script language=javascript>
function fieldSubmit() {
	var chkcnt = 0;
	
	for(i = 0; i < document.field_form.fieldIds.length ; i++) {
    	if(document.field_form.fieldIds[i].checked == true) {
    		chkcnt++;
    	}
    }
    
    if(chkcnt > 6) {
    	alert('최대 6개까지만 가능합니다.');
    	return;
    }

	document.field_form.action = 'field_submit.nhn';
	document.field_form.submit();
}

function fieldDefault() {
	document.field_form.action = 'field_del.nhn';
	document.field_form.submit();

}
</script>
<!-- 항목선택 -->
<div class="box_type_m" style="margin-top:0">
<form name='field_form'>
<input type=hidden name=menu value="market_sum">
<input type=hidden name=returnUrl value="http://finance.naver.com/sise/sise_market_sum.nhn?&page=1">
	<div class="subcnt_sise_item sub810"><div class="subcnt_sise_item_top sub810t">
		<table summary="원하시는 항목을 선택하여 결과를 보실 수 있습니다." cellpadding="0" cellspacing="0" class="item_list">
		<caption>항목 선택표</caption>
		<colgroup><col width=62><col width=84><col width=111><col width=97><col width=116><col width=85></colgroup>
		
			<tr>
			
			

			
				
				
					
				
					
				
					
				
					
						
					
				
					
				
					
				
				<td class='choice'><input type="checkbox" id="option1" name="fieldIds" value="quant"  checked> <label for="option1">거래량</label></td>
			
				
				
					
				
					
				
					
				
					
				
					
				
					
				
				<td ><input type="checkbox" id="option2" name="fieldIds" value="ask_buy"  > <label for="option2">매수호가</label></td>
			
				
				
					
				
					
				
					
				
					
				
					
				
					
				
				<td ><input type="checkbox" id="option3" name="fieldIds" value="amount"  > <label for="option3">거래대금</label>(백만)</td>
			
				
				
					
						
					
				
					
				
					
				
					
				
					
				
					
				
				<td class='choice'><input type="checkbox" id="option4" name="fieldIds" value="market_sum"  checked> <label for="option4">시가총액</label>(억)</td>
			
				
				
					
				
					
				
					
				
					
				
					
				
					
				
				<td ><input type="checkbox" id="option5" name="fieldIds" value="operating_profit"  > <label for="option5">영업이익</label>(억)</td>
			
				
				
					
				
					
				
					
				
					
				
					
						
					
				
					
				
				<td class='choice'><input type="checkbox" id="option6" name="fieldIds" value="per"  checked> <label for="option6">PER</label>(배)</td>
			
			</tr>
		
			<tr>
			
			

			
				
				
					
				
					
				
					
				
					
				
					
				
					
				
				<td ><input type="checkbox" id="option7" name="fieldIds" value="open_val"  > <label for="option7">시가</label></td>
			
				
				
					
				
					
				
					
				
					
				
					
				
					
				
				<td ><input type="checkbox" id="option8" name="fieldIds" value="ask_sell"  > <label for="option8">매도호가</label></td>
			
				
				
					
				
					
				
					
				
					
				
					
				
					
				
				<td ><input type="checkbox" id="option9" name="fieldIds" value="prev_quant"  > <label for="option9">전일거래량</label></td>
			
				
				
					
				
					
				
					
				
					
				
					
				
					
				
				<td ><input type="checkbox" id="option10" name="fieldIds" value="property_total"  > <label for="option10">자산총계</label>(억)</td>
			
				
				
					
				
					
				
					
				
					
				
					
				
					
				
				<td ><input type="checkbox" id="option11" name="fieldIds" value="operating_profit_increasing_rate"  > <label for="option11">영업이익증가율</label></td>
			
				
				
					
				
					
				
					
				
					
				
					
				
					
						
					
				
				<td class='choice'><input type="checkbox" id="option12" name="fieldIds" value="roe"  checked> <label for="option12">ROE</label>(%)</td>
			
			</tr>
		
			<tr>
			
			

			
				
				
					
				
					
				
					
				
					
				
					
				
					
				
				<td ><input type="checkbox" id="option13" name="fieldIds" value="high_val"  > <label for="option13">고가</label></td>
			
				
				
					
				
					
				
					
				
					
				
					
				
					
				
				<td ><input type="checkbox" id="option14" name="fieldIds" value="buy_total"  > <label for="option14">매수총잔량</label></td>
			
				
				
					
				
					
				
					
						
					
				
					
				
					
				
					
				
				<td class='choice'><input type="checkbox" id="option15" name="fieldIds" value="frgn_rate"  checked> <label for="option15">외국인비율</label></td>
			
				
				
					
				
					
				
					
				
					
				
					
				
					
				
				<td ><input type="checkbox" id="option16" name="fieldIds" value="debt_total"  > <label for="option16">부채총계</label>(억)</td>
			
				
				
					
				
					
				
					
				
					
				
					
				
					
				
				<td ><input type="checkbox" id="option17" name="fieldIds" value="net_income"  > <label for="option17">당기순이익</label>(억)</td>
			
				
				
					
				
					
				
					
				
					
				
					
				
					
				
				<td ><input type="checkbox" id="option18" name="fieldIds" value="roa"  > <label for="option18">ROA</label>(%)</td>
			
			</tr>
		
			<tr>
			
			

			
				
				
					
				
					
				
					
				
					
				
					
				
					
				
				<td ><input type="checkbox" id="option19" name="fieldIds" value="low_val"  > <label for="option19">저가</label></td>
			
				
				
					
				
					
				
					
				
					
				
					
				
					
				
				<td ><input type="checkbox" id="option20" name="fieldIds" value="sell_total"  > <label for="option20">매도총잔량</label></td>
			
				
				
					
				
					
						
					
				
					
				
					
				
					
				
					
				
				<td class='choice'><input type="checkbox" id="option21" name="fieldIds" value="listed_stock_cnt"  checked> <label for="option21">상장주식수</label>(천주)</td>
			
				
				
					
				
					
				
					
				
					
				
					
				
					
				
				<td ><input type="checkbox" id="option22" name="fieldIds" value="sales"  > <label for="option22">매출액</label>(억)</td>
			
				
				
					
				
					
				
					
				
					
				
					
				
					
				
				<td ><input type="checkbox" id="option23" name="fieldIds" value="eps"  > <label for="option23">주당순이익</label>(원)</td>
			
				
				
					
				
					
				
					
				
					
				
					
				
					
				
				<td ><input type="checkbox" id="option24" name="fieldIds" value="pbr"  > <label for="option24">PBR</label>(배)</td>
			
			</tr>
		
			<tr>
			
			<td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td>

			
				
				
					
				
					
				
					
				
					
				
					
				
					
				
				<td ><input type="checkbox" id="option25" name="fieldIds" value="sales_increasing_rate"  > <label for="option25">매출액증가율</label></td>
			
				
				
					
				
					
				
					
				
					
				
					
				
					
				
				<td ><input type="checkbox" id="option26" name="fieldIds" value="dividend"  > <label for="option26">보통주배당금</label>(원)</td>
			
				
				
					
				
					
				
					
				
					
				
					
				
					
				
				<td ><input type="checkbox" id="option27" name="fieldIds" value="reserve_ratio"  > <label for="option27">유보율</label>(%)</td>
			
			</tr>
		
		</table>
		<div class="item_btn">
			<a href="javascript:fieldSubmit()"><img src="https://ssl.pstatic.net/imgstock/images5/btn_apply.gif" alt="적용하기" width="55" height="18"></a><a href="javascript:fieldDefault()"><img src="https://ssl.pstatic.net/imgstock/images5/btn_initialize.gif" alt="초기항 목으로" width="76" height="18"></a>
		</div>
	</div></div>
</div>
</form>
<!-- //항목선택 끝 -->

			<!-- //항목선택 끝 -->
			</div>
			<!--  right area -->
			<div id="contentarea_right">
				


	

	
		<script>document.domain='naver.com';</script>
	

			</div>

			<!-- 종목 -->
			<div class="box_type_l">
				<div class="tab_style_1">

	
	
	
					<div class="tab_smeun choice"><div class="choice_lt"></div>코스피</div>
					<div class="tab_smeun"><a href="?sosok=1">코스닥</a></div>
	

				</div>
				
				<!-- [D] 활성화된 탭메뉴에 따라 blind text 변경해주세요 -->

	
	
				<h4 class="blind">코스피</h4>
				<table summary="코스피 시세정보를 선택한 항목에 따라 정보를 제공합니다." cellpadding="0" cellspacing="0" class="type_2">
				<caption>코스피</caption>
	


				<colgroup>
				<col width="2%">
				<col width="*">
				<col width="7%">
				<col width="9%">
				<col width="7%">
				<col width="8%">
	
					<col width="8%">
	
					<col width="8%">
	
					<col width="8%">
	
					<col width="8%">
	
					<col width="8%">
	
					<col width="8%">
	
				<col width="6%">
				</colgroup>
				<thead>
				<tr>
					<th scope="col">N</th>
					<th scope="col">종목명</th>
					<th scope="col">현재가</th>
					<th scope="col" class="tr" style="padding-right:8px">전일비</th>
					<th scope="col">등락률</th>
					<th scope="col">액면가</th>
	
					<th scope="col">시가총액</th>
	
					<th scope="col">상장주식수</th>
	
					<th scope="col">외국인비율</th>
	
					<th scope="col">거래량</th>
	
					<th scope="col">PER</th>
	
					<th scope="col">ROE</th>
	
					<th scope="col">토론실</th>
				</tr>
				</thead>
				<tbody>
				<tr><td colspan="10" class="blank_08"></td></tr>
				
				
					
					
				
				
				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">1</td>
					<td><a href="/item/main.nhn?code=005930" class="tltle">삼성전자</a></td>
					<td class="number">50,300</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				1,000
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-1.95%
				</span>
			</td>
					<td class="number">100</td>
	
		
			
			
			
									<td class="number">3,002,801</td>
			
		
	
		
			
			
			
									<td class="number">5,969,783</td>
			
		
	
		
			
			
			
									<td class="number">57.24</td>
			
		
	
		
			
			
			
									<td class="number">11,012,292</td>
			
		
	
		
			
			
			
									<td class="number">8.35</td>
			
		
	
		
			
			
			
									<td class="number">19.63</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=005930"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">2</td>
					<td><a href="/item/main.nhn?code=000660" class="tltle">SK하이닉스</a></td>
					<td class="number">80,900</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				1,900
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-2.29%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">588,954</td>
			
		
	
		
			
			
			
									<td class="number">728,002</td>
			
		
	
		
			
			
			
									<td class="number">50.61</td>
			
		
	
		
			
			
			
									<td class="number">2,015,948</td>
			
		
	
		
			
			
			
									<td class="number">3.79</td>
			
		
	
		
			
			
			
									<td class="number">38.53</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=000660"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">3</td>
					<td><a href="/item/main.nhn?code=005935" class="tltle">삼성전자우</a></td>
					<td class="number">40,850</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				850
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-2.04%
				</span>
			</td>
					<td class="number">100</td>
	
		
			
			
			
									<td class="number">336,149</td>
			
		
	
		
			
			
			
									<td class="number">822,887</td>
			
		
	
		
			
			
			
									<td class="number">92.13</td>
			
		
	
		
			
			
			
									<td class="number">1,450,354</td>
			
		
	
		
			
			
			
									<td class="number">6.78</td>
			
		
	
		
			
			
					<td class="number">N/A</td>
			
			
		
	
					<td class="center"><a href="/item/board.nhn?code=005935"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">4</td>
					<td><a href="/item/main.nhn?code=035420" class="tltle">NAVER</a></td>
					<td class="number">172,000</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				1,000
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-0.58%
				</span>
			</td>
					<td class="number">100</td>
	
		
			
			
			
									<td class="number">283,479</td>
			
		
	
		
			
			
			
									<td class="number">164,813</td>
			
		
	
		
			
			
			
									<td class="number">58.71</td>
			
		
	
		
			
			
			
									<td class="number">348,824</td>
			
		
	
		
			
			
			
									<td class="number">43.69</td>
			
		
	
		
			
			
			
									<td class="number">12.97</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=035420"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">5</td>
					<td><a href="/item/main.nhn?code=207940" class="tltle">삼성바이오로직스</a></td>
					<td class="number">393,500</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				5,500
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-1.38%
				</span>
			</td>
					<td class="number">2,500</td>
	
		
			
			
			
									<td class="number">260,359</td>
			
		
	
		
			
			
			
									<td class="number">66,165</td>
			
		
	
		
			
			
			
									<td class="number">9.85</td>
			
		
	
		
			
			
			
									<td class="number">73,962</td>
			
		
	
		
			
			
			
									<td class="number">116.18</td>
			
		
	
		
			
			
			
									<td class="number">5.51</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=207940"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
				<tr><td colspan="13" class="blank_06"></td></tr>
				<tr><td colspan="13" class="division_line"></td></tr>
				<tr><td colspan="13" class="blank_08"></td></tr>
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">6</td>
					<td><a href="/item/main.nhn?code=005380" class="tltle">현대차</a></td>
					<td class="number">121,000</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				3,000
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-2.42%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">258,538</td>
			
		
	
		
			
			
			
									<td class="number">213,668</td>
			
		
	
		
			
			
			
									<td class="number">42.12</td>
			
		
	
		
			
			
			
									<td class="number">1,015,942</td>
			
		
	
		
			
			
			
									<td class="number">22.61</td>
			
		
	
		
			
			
			
									<td class="number">2.20</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=005380"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">7</td>
					<td><a href="/item/main.nhn?code=012330" class="tltle">현대모비스</a></td>
					<td class="number">245,000</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				6,000
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-2.39%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">233,501</td>
			
		
	
		
			
			
			
									<td class="number">95,307</td>
			
		
	
		
			
			
			
									<td class="number">48.68</td>
			
		
	
		
			
			
			
									<td class="number">257,701</td>
			
		
	
		
			
			
			
									<td class="number">12.63</td>
			
		
	
		
			
			
			
									<td class="number">6.30</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=012330"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">8</td>
					<td><a href="/item/main.nhn?code=068270" class="tltle">셀트리온</a></td>
					<td class="number">174,000</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				4,500
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-2.52%
				</span>
			</td>
					<td class="number">1,000</td>
	
		
			
			
			
									<td class="number">223,308</td>
			
		
	
		
			
			
			
									<td class="number">128,338</td>
			
		
	
		
			
			
			
									<td class="number">19.94</td>
			
		
	
		
			
			
			
									<td class="number">585,214</td>
			
		
	
		
			
			
			
									<td class="number">84.92</td>
			
		
	
		
			
			
			
									<td class="number">10.84</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=068270"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">9</td>
					<td><a href="/item/main.nhn?code=051910" class="tltle">LG화학</a></td>
					<td class="number">306,500</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				2,500
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-0.81%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">216,366</td>
			
		
	
		
			
			
			
									<td class="number">70,592</td>
			
		
	
		
			
			
			
									<td class="number">38.19</td>
			
		
	
		
			
			
			
									<td class="number">158,357</td>
			
		
	
		
			
			
			
									<td class="number">16.29</td>
			
		
	
		
			
			
			
									<td class="number">8.86</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=051910"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">10</td>
					<td><a href="/item/main.nhn?code=055550" class="tltle">신한지주</a></td>
					<td class="number">43,550</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				950
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-2.13%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">206,514</td>
			
		
	
		
			
			
			
									<td class="number">474,200</td>
			
		
	
		
			
			
			
									<td class="number">64.89</td>
			
		
	
		
			
			
			
									<td class="number">991,471</td>
			
		
	
		
			
			
			
									<td class="number">6.54</td>
			
		
	
		
			
			
			
									<td class="number">9.21</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=055550"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
				<tr><td colspan="13" class="blank_06"></td></tr>
				<tr><td colspan="13" class="division_line"></td></tr>
				<tr><td colspan="13" class="blank_08"></td></tr>
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">11</td>
					<td><a href="/item/main.nhn?code=005490" class="tltle">POSCO</a></td>
					<td class="number">230,500</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				2,000
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-0.86%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">200,966</td>
			
		
	
		
			
			
			
									<td class="number">87,187</td>
			
		
	
		
			
			
			
									<td class="number">52.20</td>
			
		
	
		
			
			
			
									<td class="number">255,627</td>
			
		
	
		
			
			
			
									<td class="number">11.89</td>
			
		
	
		
			
			
			
									<td class="number">3.88</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=005490"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">12</td>
					<td><a href="/item/main.nhn?code=017670" class="tltle">SK텔레콤</a></td>
					<td class="number">246,000</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				500
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-0.20%
				</span>
			</td>
					<td class="number">500</td>
	
		
			
			
			
									<td class="number">198,634</td>
			
		
	
		
			
			
			
									<td class="number">80,746</td>
			
		
	
		
			
			
			
									<td class="number">37.76</td>
			
		
	
		
			
			
			
									<td class="number">162,428</td>
			
		
	
		
			
			
			
									<td class="number">6.35</td>
			
		
	
		
			
			
			
									<td class="number">15.52</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=017670"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">13</td>
					<td><a href="/item/main.nhn?code=051900" class="tltle">LG생활건강</a></td>
					<td class="number">1,265,000</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				25,000
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-1.94%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">197,570</td>
			
		
	
		
			
			
			
									<td class="number">15,618</td>
			
		
	
		
			
			
			
									<td class="number">45.15</td>
			
		
	
		
			
			
			
									<td class="number">30,107</td>
			
		
	
		
			
			
			
									<td class="number">32.83</td>
			
		
	
		
			
			
			
									<td class="number">20.98</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=051900"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">14</td>
					<td><a href="/item/main.nhn?code=105560" class="tltle">KB금융</a></td>
					<td class="number">46,050</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				500
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-1.07%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">192,540</td>
			
		
	
		
			
			
			
									<td class="number">418,112</td>
			
		
	
		
			
			
			
									<td class="number">66.72</td>
			
		
	
		
			
			
			
									<td class="number">753,534</td>
			
		
	
		
			
			
			
									<td class="number">6.29</td>
			
		
	
		
			
			
			
									<td class="number">8.78</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=105560"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">15</td>
					<td><a href="/item/main.nhn?code=028260" class="tltle">삼성물산</a></td>
					<td class="number">98,900</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				2,600
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-2.56%
				</span>
			</td>
					<td class="number">100</td>
	
		
			
			
			
									<td class="number">187,603</td>
			
		
	
		
			
			
			
									<td class="number">189,690</td>
			
		
	
		
			
			
			
									<td class="number">13.78</td>
			
		
	
		
			
			
			
									<td class="number">301,389</td>
			
		
	
		
			
			
			
									<td class="number">11.05</td>
			
		
	
		
			
			
			
									<td class="number">8.06</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=028260"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
				<tr><td colspan="13" class="blank_06"></td></tr>
				<tr><td colspan="13" class="division_line"></td></tr>
				<tr><td colspan="13" class="blank_08"></td></tr>
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">16</td>
					<td><a href="/item/main.nhn?code=034730" class="tltle">SK</a></td>
					<td class="number">257,500</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				2,500
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-0.96%
				</span>
			</td>
					<td class="number">200</td>
	
		
			
			
			
									<td class="number">181,178</td>
			
		
	
		
			
			
			
									<td class="number">70,360</td>
			
		
	
		
			
			
			
									<td class="number">25.48</td>
			
		
	
		
			
			
			
									<td class="number">166,041</td>
			
		
	
		
			
			
			
									<td class="number">8.11</td>
			
		
	
		
			
			
			
									<td class="number">14.88</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=034730"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">17</td>
					<td><a href="/item/main.nhn?code=015760" class="tltle">한국전력</a></td>
					<td class="number">27,900</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_up.gif" width="7" height="6" style="margin-right:4px;" alt="상승"><span class="tah p11 red02">
				400
				</span>
			</td>
					<td class="number">
				<span class="tah p11 red01">
				+1.45%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">179,108</td>
			
		
	
		
			
			
			
									<td class="number">641,964</td>
			
		
	
		
			
			
			
									<td class="number">25.51</td>
			
		
	
		
			
			
			
									<td class="number">2,574,274</td>
			
		
	
		
			
			
			
									<td class="number">-13.62</td>
			
		
	
		
			
			
			
									<td class="number">-1.86</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=015760"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">18</td>
					<td><a href="/item/main.nhn?code=000270" class="tltle">기아차</a></td>
					<td class="number">43,250</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				1,300
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-2.92%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">175,320</td>
			
		
	
		
			
			
			
									<td class="number">405,363</td>
			
		
	
		
			
			
			
									<td class="number">42.35</td>
			
		
	
		
			
			
			
									<td class="number">860,109</td>
			
		
	
		
			
			
			
									<td class="number">15.16</td>
			
		
	
		
			
			
			
									<td class="number">4.27</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=000270"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">19</td>
					<td><a href="/item/main.nhn?code=006400" class="tltle">삼성SDI</a></td>
					<td class="number">231,000</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				2,000
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-0.86%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">158,846</td>
			
		
	
		
			
			
			
									<td class="number">68,765</td>
			
		
	
		
			
			
			
									<td class="number">43.67</td>
			
		
	
		
			
			
			
									<td class="number">139,394</td>
			
		
	
		
			
			
			
									<td class="number">23.19</td>
			
		
	
		
			
			
			
									<td class="number">6.05</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=006400"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">20</td>
					<td><a href="/item/main.nhn?code=018260" class="tltle">삼성에스디에스</a></td>
					<td class="number">195,500</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				3,500
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-1.76%
				</span>
			</td>
					<td class="number">500</td>
	
		
			
			
			
									<td class="number">151,274</td>
			
		
	
		
			
			
			
									<td class="number">77,378</td>
			
		
	
		
			
			
			
									<td class="number">12.87</td>
			
		
	
		
			
			
			
									<td class="number">68,754</td>
			
		
	
		
			
			
			
									<td class="number">24.03</td>
			
		
	
		
			
			
			
									<td class="number">10.91</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=018260"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
				<tr><td colspan="13" class="blank_06"></td></tr>
				<tr><td colspan="13" class="division_line"></td></tr>
				<tr><td colspan="13" class="blank_08"></td></tr>
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">21</td>
					<td><a href="/item/main.nhn?code=032830" class="tltle">삼성생명</a></td>
					<td class="number">71,600</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				1,100
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-1.51%
				</span>
			</td>
					<td class="number">500</td>
	
		
			
			
			
									<td class="number">143,200</td>
			
		
	
		
			
			
			
									<td class="number">200,000</td>
			
		
	
		
			
			
			
									<td class="number">15.74</td>
			
		
	
		
			
			
			
									<td class="number">181,471</td>
			
		
	
		
			
			
			
									<td class="number">8.60</td>
			
		
	
		
			
			
			
									<td class="number">5.95</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=032830"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">22</td>
					<td><a href="/item/main.nhn?code=096770" class="tltle">SK이노베이션</a></td>
					<td class="number">146,500</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				1,000
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-0.68%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">135,462</td>
			
		
	
		
			
			
			
									<td class="number">92,466</td>
			
		
	
		
			
			
			
									<td class="number">35.28</td>
			
		
	
		
			
			
			
									<td class="number">231,612</td>
			
		
	
		
			
			
			
									<td class="number">8.31</td>
			
		
	
		
			
			
			
									<td class="number">9.12</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=096770"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">23</td>
					<td><a href="/item/main.nhn?code=033780" class="tltle">KT&G</a></td>
					<td class="number">97,800</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				900
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-0.91%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">134,272</td>
			
		
	
		
			
			
			
									<td class="number">137,292</td>
			
		
	
		
			
			
			
									<td class="number">48.65</td>
			
		
	
		
			
			
			
									<td class="number">313,408</td>
			
		
	
		
			
			
			
									<td class="number">14.89</td>
			
		
	
		
			
			
			
									<td class="number">11.38</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=033780"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">24</td>
					<td><a href="/item/main.nhn?code=035720" class="tltle">카카오</a></td>
					<td class="number">155,500</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				1,500
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-0.96%
				</span>
			</td>
					<td class="number">500</td>
	
		
			
			
			
									<td class="number">133,850</td>
			
		
	
		
			
			
			
									<td class="number">86,077</td>
			
		
	
		
			
			
			
									<td class="number">30.24</td>
			
		
	
		
			
			
			
									<td class="number">470,820</td>
			
		
	
		
			
			
			
									<td class="number">253.67</td>
			
		
	
		
			
			
			
									<td class="number">1.05</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=035720"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">25</td>
					<td><a href="/item/main.nhn?code=003550" class="tltle">LG</a></td>
					<td class="number">71,000</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				1,300
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-1.80%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">122,516</td>
			
		
	
		
			
			
			
									<td class="number">172,557</td>
			
		
	
		
			
			
			
									<td class="number">34.64</td>
			
		
	
		
			
			
			
									<td class="number">171,353</td>
			
		
	
		
			
			
			
									<td class="number">6.70</td>
			
		
	
		
			
			
			
									<td class="number">10.96</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=003550"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
				<tr><td colspan="13" class="blank_06"></td></tr>
				<tr><td colspan="13" class="division_line"></td></tr>
				<tr><td colspan="13" class="blank_08"></td></tr>
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">26</td>
					<td><a href="/item/main.nhn?code=066570" class="tltle">LG전자</a></td>
					<td class="number">69,900</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				1,100
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-1.55%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">114,390</td>
			
		
	
		
			
			
			
									<td class="number">163,648</td>
			
		
	
		
			
			
			
									<td class="number">33.85</td>
			
		
	
		
			
			
			
									<td class="number">350,104</td>
			
		
	
		
			
			
			
									<td class="number">10.19</td>
			
		
	
		
			
			
			
									<td class="number">9.03</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=066570"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">27</td>
					<td><a href="/item/main.nhn?code=090430" class="tltle">아모레퍼시픽</a></td>
					<td class="number">189,000</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				2,500
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-1.31%
				</span>
			</td>
					<td class="number">500</td>
	
		
			
			
			
									<td class="number">110,487</td>
			
		
	
		
			
			
			
									<td class="number">58,458</td>
			
		
	
		
			
			
			
									<td class="number">31.84</td>
			
		
	
		
			
			
			
									<td class="number">436,753</td>
			
		
	
		
			
			
			
									<td class="number">39.27</td>
			
		
	
		
			
			
			
									<td class="number">7.75</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=090430"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">28</td>
					<td><a href="/item/main.nhn?code=000810" class="tltle">삼성화재</a></td>
					<td class="number">232,500</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				7,500
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-3.12%
				</span>
			</td>
					<td class="number">500</td>
	
		
			
			
			
									<td class="number">110,146</td>
			
		
	
		
			
			
			
									<td class="number">47,375</td>
			
		
	
		
			
			
			
									<td class="number">47.97</td>
			
		
	
		
			
			
			
									<td class="number">110,600</td>
			
		
	
		
			
			
			
									<td class="number">10.98</td>
			
		
	
		
			
			
			
									<td class="number">8.81</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=000810"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">29</td>
					<td><a href="/item/main.nhn?code=036570" class="tltle">엔씨소프트</a></td>
					<td class="number">493,000</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				6,000
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-1.20%
				</span>
			</td>
					<td class="number">500</td>
	
		
			
			
			
									<td class="number">108,233</td>
			
		
	
		
			
			
			
									<td class="number">21,954</td>
			
		
	
		
			
			
			
									<td class="number">49.87</td>
			
		
	
		
			
			
			
									<td class="number">128,217</td>
			
		
	
		
			
			
			
									<td class="number">25.86</td>
			
		
	
		
			
			
			
									<td class="number">16.44</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=036570"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">30</td>
					<td><a href="/item/main.nhn?code=086790" class="tltle">하나금융지주</a></td>
					<td class="number">35,750</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				550
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-1.52%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">107,337</td>
			
		
	
		
			
			
			
									<td class="number">300,242</td>
			
		
	
		
			
			
			
									<td class="number">67.04</td>
			
		
	
		
			
			
			
									<td class="number">780,728</td>
			
		
	
		
			
			
			
									<td class="number">4.79</td>
			
		
	
		
			
			
			
									<td class="number">8.88</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=086790"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
				<tr><td colspan="13" class="blank_06"></td></tr>
				<tr><td colspan="13" class="division_line"></td></tr>
				<tr><td colspan="13" class="blank_08"></td></tr>
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">31</td>
					<td><a href="/item/main.nhn?code=010950" class="tltle">S-Oil</a></td>
					<td class="number">89,200</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				1,600
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-1.76%
				</span>
			</td>
					<td class="number">2,500</td>
	
		
			
			
			
									<td class="number">100,424</td>
			
		
	
		
			
			
			
									<td class="number">112,583</td>
			
		
	
		
			
			
			
									<td class="number">79.46</td>
			
		
	
		
			
			
			
									<td class="number">328,724</td>
			
		
	
		
			
			
			
									<td class="number">40.31</td>
			
		
	
		
			
			
			
									<td class="number">3.88</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=010950"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">32</td>
					<td><a href="/item/main.nhn?code=009540" class="tltle">한국조선해양</a></td>
					<td class="number">120,000</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				2,000
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-1.64%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">84,928</td>
			
		
	
		
			
			
			
									<td class="number">70,773</td>
			
		
	
		
			
			
			
									<td class="number">16.90</td>
			
		
	
		
			
			
			
									<td class="number">101,703</td>
			
		
	
		
			
			
			
									<td class="number">-16.45</td>
			
		
	
		
			
			
			
									<td class="number">-4.25</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=009540"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">33</td>
					<td><a href="/item/main.nhn?code=316140" class="tltle">우리금융지주</a></td>
					<td class="number">11,700</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				100
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-0.85%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">84,505</td>
			
		
	
		
			
			
			
									<td class="number">722,268</td>
			
		
	
		
			
			
			
									<td class="number">31.57</td>
			
		
	
		
			
			
			
									<td class="number">2,060,420</td>
			
		
	
		
			
			
					<td class="number">N/A</td>
			
			
		
	
		
			
			
					<td class="number">N/A</td>
			
			
		
	
					<td class="center"><a href="/item/board.nhn?code=316140"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">34</td>
					<td><a href="/item/main.nhn?code=009150" class="tltle">삼성전기</a></td>
					<td class="number">111,000</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				1,000
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-0.89%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">82,910</td>
			
		
	
		
			
			
			
									<td class="number">74,694</td>
			
		
	
		
			
			
			
									<td class="number">26.64</td>
			
		
	
		
			
			
			
									<td class="number">447,765</td>
			
		
	
		
			
			
			
									<td class="number">13.13</td>
			
		
	
		
			
			
			
									<td class="number">14.50</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=009150"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">35</td>
					<td><a href="/item/main.nhn?code=010130" class="tltle">고려아연</a></td>
					<td class="number">406,000</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				6,000
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-1.46%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">76,612</td>
			
		
	
		
			
			
			
									<td class="number">18,870</td>
			
		
	
		
			
			
			
									<td class="number">26.78</td>
			
		
	
		
			
			
			
									<td class="number">32,384</td>
			
		
	
		
			
			
			
									<td class="number">14.53</td>
			
		
	
		
			
			
			
									<td class="number">8.64</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=010130"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
				<tr><td colspan="13" class="blank_06"></td></tr>
				<tr><td colspan="13" class="division_line"></td></tr>
				<tr><td colspan="13" class="blank_08"></td></tr>
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">36</td>
					<td><a href="/item/main.nhn?code=251270" class="tltle">넷마블</a></td>
					<td class="number">88,000</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				1,000
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-1.12%
				</span>
			</td>
					<td class="number">100</td>
	
		
			
			
			
									<td class="number">75,454</td>
			
		
	
		
			
			
			
									<td class="number">85,743</td>
			
		
	
		
			
			
			
									<td class="number">22.56</td>
			
		
	
		
			
			
			
									<td class="number">156,339</td>
			
		
	
		
			
			
			
									<td class="number">39.53</td>
			
		
	
		
			
			
			
									<td class="number">4.36</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=251270"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">37</td>
					<td><a href="/item/main.nhn?code=011170" class="tltle">롯데케미칼</a></td>
					<td class="number">220,000</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				2,000
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-0.90%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">75,406</td>
			
		
	
		
			
			
			
									<td class="number">34,275</td>
			
		
	
		
			
			
			
									<td class="number">30.81</td>
			
		
	
		
			
			
			
									<td class="number">128,610</td>
			
		
	
		
			
			
			
									<td class="number">4.77</td>
			
		
	
		
			
			
			
									<td class="number">13.04</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=011170"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">38</td>
					<td><a href="/item/main.nhn?code=030200" class="tltle">KT</a></td>
					<td class="number">26,950</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				300
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-1.10%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">70,370</td>
			
		
	
		
			
			
			
									<td class="number">261,112</td>
			
		
	
		
			
			
			
									<td class="number">48.30</td>
			
		
	
		
			
			
			
									<td class="number">612,548</td>
			
		
	
		
			
			
			
									<td class="number">10.22</td>
			
		
	
		
			
			
			
									<td class="number">5.50</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=030200"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">39</td>
					<td><a href="/item/main.nhn?code=069500" class="tltle">KODEX 200</a></td>
					<td class="number">27,700</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				485
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-1.72%
				</span>
			</td>
					<td class="number">0</td>
	
		
			
			
			
									<td class="number">69,375</td>
			
		
	
		
			
			
			
									<td class="number">250,450</td>
			
		
	
		
			
			
			
									<td class="number">9.46</td>
			
		
	
		
			
			
			
									<td class="number">3,594,047</td>
			
		
	
		
			
			
					<td class="number">N/A</td>
			
			
		
	
		
			
			
					<td class="number">N/A</td>
			
			
		
	
					<td class="center"><a href="/item/board.nhn?code=069500"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">40</td>
					<td><a href="/item/main.nhn?code=024110" class="tltle">기업은행</a></td>
					<td class="number">11,750</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				150
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-1.26%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">67,816</td>
			
		
	
		
			
			
			
									<td class="number">577,157</td>
			
		
	
		
			
			
			
									<td class="number">20.57</td>
			
		
	
		
			
			
			
									<td class="number">2,043,125</td>
			
		
	
		
			
			
			
									<td class="number">4.41</td>
			
		
	
		
			
			
			
									<td class="number">8.63</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=024110"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
				<tr><td colspan="13" class="blank_06"></td></tr>
				<tr><td colspan="13" class="division_line"></td></tr>
				<tr><td colspan="13" class="blank_08"></td></tr>
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">41</td>
					<td><a href="/item/main.nhn?code=002790" class="tltle">아모레G</a></td>
					<td class="number">81,200</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				900
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-1.10%
				</span>
			</td>
					<td class="number">500</td>
	
		
			
			
			
									<td class="number">66,956</td>
			
		
	
		
			
			
			
									<td class="number">82,458</td>
			
		
	
		
			
			
			
									<td class="number">21.73</td>
			
		
	
		
			
			
			
									<td class="number">149,788</td>
			
		
	
		
			
			
			
									<td class="number">50.75</td>
			
		
	
		
			
			
			
									<td class="number">4.65</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=002790"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">42</td>
					<td><a href="/item/main.nhn?code=021240" class="tltle">웅진코웨이</a></td>
					<td class="number">89,600</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				3,300
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-3.55%
				</span>
			</td>
					<td class="number">500</td>
	
		
			
			
			
									<td class="number">66,124</td>
			
		
	
		
			
			
			
									<td class="number">73,800</td>
			
		
	
		
			
			
			
									<td class="number">59.64</td>
			
		
	
		
			
			
			
									<td class="number">220,018</td>
			
		
	
		
			
			
			
									<td class="number">18.92</td>
			
		
	
		
			
			
			
									<td class="number">33.84</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=021240"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">43</td>
					<td><a href="/item/main.nhn?code=035250" class="tltle">강원랜드</a></td>
					<td class="number">29,350</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				800
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-2.65%
				</span>
			</td>
					<td class="number">500</td>
	
		
			
			
			
									<td class="number">62,792</td>
			
		
	
		
			
			
			
									<td class="number">213,940</td>
			
		
	
		
			
			
			
									<td class="number">30.35</td>
			
		
	
		
			
			
			
									<td class="number">370,969</td>
			
		
	
		
			
			
			
									<td class="number">21.12</td>
			
		
	
		
			
			
			
									<td class="number">8.39</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=035250"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">44</td>
					<td><a href="/item/main.nhn?code=032640" class="tltle">LG유플러스</a></td>
					<td class="number">13,400</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				200
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-1.47%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">58,506</td>
			
		
	
		
			
			
			
									<td class="number">436,611</td>
			
		
	
		
			
			
			
									<td class="number">37.11</td>
			
		
	
		
			
			
			
									<td class="number">1,675,094</td>
			
		
	
		
			
			
			
									<td class="number">12.15</td>
			
		
	
		
			
			
			
									<td class="number">7.97</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=032640"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">45</td>
					<td><a href="/item/main.nhn?code=018880" class="tltle">한온시스템</a></td>
					<td class="number">10,800</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_up.gif" width="7" height="6" style="margin-right:4px;" alt="상승"><span class="tah p11 red02">
				50
				</span>
			</td>
					<td class="number">
				<span class="tah p11 red01">
				+0.47%
				</span>
			</td>
					<td class="number">100</td>
	
		
			
			
			
									<td class="number">57,650</td>
			
		
	
		
			
			
			
									<td class="number">533,800</td>
			
		
	
		
			
			
			
									<td class="number">19.23</td>
			
		
	
		
			
			
			
									<td class="number">516,859</td>
			
		
	
		
			
			
			
									<td class="number">20.77</td>
			
		
	
		
			
			
			
									<td class="number">13.83</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=018880"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
				<tr><td colspan="13" class="blank_06"></td></tr>
				<tr><td colspan="13" class="division_line"></td></tr>
				<tr><td colspan="13" class="blank_08"></td></tr>
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">46</td>
					<td><a href="/item/main.nhn?code=086280" class="tltle">현대글로비스</a></td>
					<td class="number">150,500</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				1,500
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-0.99%
				</span>
			</td>
					<td class="number">500</td>
	
		
			
			
			
									<td class="number">56,438</td>
			
		
	
		
			
			
			
									<td class="number">37,500</td>
			
		
	
		
			
			
			
									<td class="number">37.04</td>
			
		
	
		
			
			
			
									<td class="number">46,011</td>
			
		
	
		
			
			
			
									<td class="number">12.90</td>
			
		
	
		
			
			
			
									<td class="number">10.60</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=086280"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">47</td>
					<td><a href="/item/main.nhn?code=267250" class="tltle">현대중공업지주</a></td>
					<td class="number">346,000</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_up.gif" width="7" height="6" style="margin-right:4px;" alt="상승"><span class="tah p11 red02">
				1,000
				</span>
			</td>
					<td class="number">
				<span class="tah p11 red01">
				+0.29%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">56,352</td>
			
		
	
		
			
			
			
									<td class="number">16,287</td>
			
		
	
		
			
			
			
									<td class="number">19.78</td>
			
		
	
		
			
			
			
									<td class="number">31,662</td>
			
		
	
		
			
			
			
									<td class="number">20.98</td>
			
		
	
		
			
			
			
									<td class="number">3.53</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=267250"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">48</td>
					<td><a href="/item/main.nhn?code=034220" class="tltle">LG디스플레이</a></td>
					<td class="number">14,700</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				50
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-0.34%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">52,599</td>
			
		
	
		
			
			
			
									<td class="number">357,816</td>
			
		
	
		
			
			
			
									<td class="number">21.33</td>
			
		
	
		
			
			
			
									<td class="number">3,427,985</td>
			
		
	
		
			
			
			
									<td class="number">-25.39</td>
			
		
	
		
			
			
			
									<td class="number">-1.46</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=034220"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">49</td>
					<td><a href="/item/main.nhn?code=006800" class="tltle">미래에셋대우</a></td>
					<td class="number">7,230</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				110
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-1.50%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">47,596</td>
			
		
	
		
			
			
			
									<td class="number">658,316</td>
			
		
	
		
			
			
			
									<td class="number">15.26</td>
			
		
	
		
			
			
			
									<td class="number">941,808</td>
			
		
	
		
			
			
			
									<td class="number">12.55</td>
			
		
	
		
			
			
			
									<td class="number">5.83</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=006800"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
	


				<tr  onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
					<td class="no">50</td>
					<td><a href="/item/main.nhn?code=000720" class="tltle">현대건설</a></td>
					<td class="number">40,950</td>
					<td class="number">
				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
				800
				</span>
			</td>
					<td class="number">
				<span class="tah p11 nv01">
				-1.92%
				</span>
			</td>
					<td class="number">5,000</td>
	
		
			
			
			
									<td class="number">45,600</td>
			
		
	
		
			
			
			
									<td class="number">111,356</td>
			
		
	
		
			
			
			
									<td class="number">22.51</td>
			
		
	
		
			
			
			
									<td class="number">453,819</td>
			
		
	
		
			
			
			
									<td class="number">11.96</td>
			
		
	
		
			
			
			
									<td class="number">5.99</td>
			
		
	
					<td class="center"><a href="/item/board.nhn?code=000720"><img src="https://ssl.pstatic.net/imgstock/images5/ico_debatebl2.gif" width="15" height="13" alt="토론실"></a></td>
				</tr>
			
	
		
		
				<tr><td colspan="13" class="blank_09"></td></tr>
				<tr><td colspan="13" class="division_line_1"></td></tr>
				<tr><td colspan="13" class="blank_09"></td></tr>
		
	



				</tbody>
				</table>
				<table summary="페이지 네비게이션 리스트" class="Nnavi" align="center">
				<caption>페이지 네비게이션</caption>
				<tr>		
					
					
					
					<td class="on">
				<a href="/sise/sise_market_sum.nhn?&amp;page=1"  >1</a>
				</td>
<td>
				<a href="/sise/sise_market_sum.nhn?&amp;page=2"  >2</a>
				</td>
<td>
				<a href="/sise/sise_market_sum.nhn?&amp;page=3"  >3</a>
				</td>
<td>
				<a href="/sise/sise_market_sum.nhn?&amp;page=4"  >4</a>
				</td>
<td>
				<a href="/sise/sise_market_sum.nhn?&amp;page=5"  >5</a>
				</td>
<td>
				<a href="/sise/sise_market_sum.nhn?&amp;page=6"  >6</a>
				</td>
<td>
				<a href="/sise/sise_market_sum.nhn?&amp;page=7"  >7</a>
				</td>
<td>
				<a href="/sise/sise_market_sum.nhn?&amp;page=8"  >8</a>
				</td>
<td>
				<a href="/sise/sise_market_sum.nhn?&amp;page=9"  >9</a>
				</td>
<td>
				<a href="/sise/sise_market_sum.nhn?&amp;page=10"  >10</a>
				</td>

					<td class="pgR">
				<a href="/sise/sise_market_sum.nhn?&amp;page=11"  >
				다음<img src="https://ssl.pstatic.net/static/n/cmn/bu_pgarR.gif" width="3" height="5" alt="" border="0">
				</a>
				</td>

					<td class="pgRR">
				<a href="/sise/sise_market_sum.nhn?&amp;page=32"  >맨뒤
				<img src="https://ssl.pstatic.net/static/n/cmn/bu_pgarRR.gif" width="8" height="5" alt="" border="0">
				</a>
				</td>

					
				</tr>
				</table>
			</div>
			<!-- // 종목 -->
			<!-- //컨텐츠 -->
		</div>
	</div>






	






	<div id="footer">
		<ul>
			<li class="first">
				<a href="https://www.naver.com/rules/service.html" onClick="clickcr(this, 'fot.service', '', '', event);" target="_blank">이용약관</a>
			</li>
			<li>
				<a href="https://finance.naver.com/rules.nhn" onClick="clickcr(this, 'fot.policy', '', '', event);" target="_blank">금융게시판 운영원칙</a>
			</li>
			<li>
				<a href="https://www.naver.com/rules/privacy.html" onClick="clickcr(this, 'fot.privacy', '', '', event);" target="_blank"><strong>개인정보처리방침</strong></a>
			</li>
			<li>
				<a href="https://www.naver.com/rules/disclaimer.html" onClick="clickcr(this, 'fot.limit', '', '', event);" target="_blank">책임의 한계와 법적고지</a>
			</li>
			<li>
				<a href="https://help.naver.com/support/alias/contents2/finance/finance_1.naver" onclick="clickcr(this, 'fot.help', '', '', event);" target="_blank">금융 고객센터</a>
			</li>
		</ul>
		<p class="desc">네이버(주)에서 제공하는 금융정보는 각 컨텐츠 제공업체<a href="javascript:;" onclick="togglePanelFooter('footerPanel0');" class="desc_help"><img src="https://ssl.pstatic.net/static/nfinance/2018/06/29/btn_help.png" width="17" height="17" alt="제공업체 상세설명"></a>부터 받는 정보로 투자 참고 사항이며, 오류가 발생할 수 있고 지연될 수<br>있습니다. 네이버(주)는 제공된 정보에 의한 투자결과에 대한 법적인 책임을 지지 않습니다. 게시된 정보를 무단으로 배포할 수 없습니다.</p>
		<div id="footerPanel0" class="provider_layer" style="display:none" tabindex="0" onblur="hidePannel('footerPanel0')">
			<strong class="provider_layer__tit">컨텐츠 제공업체</strong>
			<div class="provider_layer__txt">
				<p><span>코스콤 : </span>실시간 주가정보 및 국내시세정보</p>
				<p><span>에프앤가이드 : </span>기업 및 재무정보</p>
				<p><span>이데일리 : </span>해외 시세 및 시장지표 정보</p>
				<p><span>제로인 : </span>펀드정보</p>
				<p><span>한국예탁결제원 : </span>주주총회일 및 전자투표 정보</p>
			</div>
			<span class="arrow"></span>
		</div>
		<address>
			<a href="https://www.navercorp.com/" target="_blank" class="logo" onClick="clickcr(this, 'fot.nhn', '', '', event);"><img src="https://ssl.pstatic.net/static/nfinance/2019/02/22/ci_naver.png" width="58" height="11" alt="NAVER" /></a>
			<em>Copyright &copy;</em>
			<a href="https://www.navercorp.com/" target="_blank" onClick="clickcr(this, 'fot.nhn', '', '', event);">NAVER Corp.</a>
			<span>All Rights Reserved.</span>
		</address>
		
		
		
	</div>



<script type="text/javascript">
function isVisible(obj) {
    if (obj == document) return true
 
    if (!obj) return false
    if (!obj.parentNode) return false
    if (obj.style) {
        if (obj.style.display == 'none') return false
        if (obj.style.visibility == 'hidden') return false
    }
 
    if (window.getComputedStyle) {
        var style = window.getComputedStyle(obj, "")
        if (style.display == 'none') return false
        if (style.visibility == 'hidden') return false
    }
 
    var style = obj.currentStyle
    if (style) {
        if (style['display'] == 'none') return false
        if (style['visibility'] == 'hidden') return false
    }
 
    return isVisible(obj.parentNode)
}

function isChildOf(myobj, containerObj) {
	while(myobj != undefined) {
		if (myobj == document.body) {
			break;
		} 
		if (myobj == containerObj) {
			return true;
		}
		myobj = myobj.parentElement;
	}
	return false;	
}

function gnbLayerClose(e){
	var target = e.target ? e.target : e.srcElement;
	if (isVisible(document.getElementById('gnb_service_lyr')) || isVisible(document.getElementById('gnb_notice_lyr')) ||isVisible(document.getElementById('gnb_my_lyr')) ) {
		if (!isChildOf(target, document.getElementById('gnb'))) {
			gnbAllLayerClose();
		}
	}	
}

var isIE = (navigator.userAgent.toLowerCase().indexOf("msie")!=-1 && window.document.all) ? true:false;
if (isIE) {
	document.attachEvent('onmousedown', gnbLayerClose);
} else {
	window.addEventListener('mousedown', gnbLayerClose);
}

function showPannel(layerId){
    var layer = jindo.$(layerId);
    layer.style.display='block';

    if (layerId == "summary_lyr") {
        var layerHeight = jindo.$Element(layer).height();
        jindo.$Element("summary_ifr").height(layerHeight);
    }
}

function hidePannel(layerId){
    var layer = jindo.$(layerId);
    layer.style.display='none';
}

function togglePanelFooter(layerId) {
    var elTargetLayer = jindo.$Element(jindo.$$.getSingle("#" + layerId));

    if (elTargetLayer != null) {
        if (elTargetLayer.visible()) {
            hidePannel(layerId);
        } else {
            showPannel(layerId);
        }
    }
}

// add data-useragent
document.documentElement.setAttribute('data-useragent',navigator.userAgent);
</script>
</div>
</body>
</html>

'''
from bs4 import BeautifulSoup

# 010-3588-6265 김경록
# 13일 오후 7시 교대역 2시간

def parse(pageString):
    # table > tr > td[1]
    bsobj = BeautifulSoup(pageString, "html.parser")
    table = bsobj.find("table", {"class":"type_2"})
    trs = table.findAll("tr")

    for tr in trs:
        try:
            td = tr.findAll("td")[1]
            print(td.text)
        except:
            # print("error")
            pass


parse(pageString)
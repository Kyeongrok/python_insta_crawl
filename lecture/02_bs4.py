pageString = '''
<html lang="ko"><head>
		<meta charset="utf-8">
		<meta property="og:url" content="https://www.tistory.com">
		<meta property="og:site_name" content="TISTORY">
		<meta property="og:title" content="TISTORY">
		<meta property="og:description" content="나를 표현하는 블로그를 만들어보세요.">
		<meta property="og:image" content="//t1.daumcdn.net/tistory_admin/static/images/openGraph/opengraph.png">
		<title>로그인 - TISTORY</title>
		<link rel="shortcut icon" href="//t1.daumcdn.net/tistory_admin/static/top/favicon.ico">
		<link rel="apple-touch-icon" href="//t1.daumcdn.net/tistory_admin/static/images/openGraph/180x180.png">
		<link rel="apple-touch-icon" sizes="76x76" href="//t1.daumcdn.net/tistory_admin/static/images/openGraph/76x76.png">
		<link rel="apple-touch-icon" sizes="120x120" href="//t1.daumcdn.net/tistory_admin/static/images/openGraph/120x120.png">
		<link rel="apple-touch-icon" sizes="152x152" href="//t1.daumcdn.net/tistory_admin/static/images/openGraph/152x152.png">
		<link rel="stylesheet" type="text/css" href="//t1.daumcdn.net/tistory_admin/www/style/top/font.css">
		<link rel="stylesheet" type="text/css" href="https://t1.daumcdn.net/tistory_admin/assets/tistory-gnb/3.1.7/gnb.min.css">
		<link rel="stylesheet" type="text/css" href="//t1.daumcdn.net/tistory_admin/assets/tistory-web-top/1574742493/static/css/pc/top.css">

<!--[if lt IE 9]>
<script src="https://t1.daumcdn.net/tistory_admin/lib/jquery-1.12.4.min.js"></script>
<![endif]-->
<!--[if gte IE 9]><!-->
<script src="https://t1.daumcdn.net/tistory_admin/lib/jquery-3.1.0.min.js"></script>
<!--<![endif]-->
<script src="https://t1.daumcdn.net/tistory_admin/lib/fingerprint2-1.4.2.min.js"></script>
<script type="text/javascript" src="//m1.daumcdn.net/svc/original/U03/cssjs/jquery/plugin/jquery.cookie-1.4.0.min.js"></script>
<script type="text/javascript" src="//s1.daumcdn.net/svc/original/U03/cssjs/userAgent/userAgent-1.0.14.min.js"></script>
	</head>
	<body>
		<div id="kakaoIndex"><!-- 웹접근성용 바로가기 링크 모음 -->
			<a href="#kakaoBody">본문 바로가기</a>
			<a href="#kakaoLnb">메뉴 바로가기</a> <!-- 2017-05-31 수정 : href 값 kakaoGnb -> kakaoLnb 로 변경 -->
		</div>
	
		<div id="kakaoWrap" class="">
			<div id="kakaoHead" role="banner" class="kakao_head head_type1">
				<div class="inner_header">
					<h1>
						<a href="/" id="kakaoServiceLogo" class="link_logo">
							<span class="img_common_tistory tit_tistory tit_tistory_white">티스토리</span>
							<span class="img_common_tistory tit_tistory tit_tistory_black"></span>
						</a>
					</h1>
					<div class="info_tistory">
						<div class="logn_tistory" style="display:block">
							<a href="/member/join" class="btn_tistory btn_log_info">가입하기</a>
						</div>
					</div>
				</div>
			</div>
			<hr class="hide">
			<div id="kakaoContent" role="main">
				<div id="cMain"> <!-- 좌측메뉴 없을 경우 : article_only 클래스 추가 -->
					<div id="mArticle">
<div class="content_login" style="background-image:url(//t1.daumcdn.net/tistory_admin/static/top/pc/bg_login_white.png)">
	<div class="inner_login">
		<div class="login_tistory ">
			<h2 class="screen_out">로그인</h2>
			<strong class="tit_login">
				<em>ID/PW</em>가 일치하지 않습니다.
			</strong>
			<form method="post" id="authForm" action="https://www.tistory.com/auth/login">
				<input type="hidden" name="redirectUrl" value="https://krksap.tistory.com/manage">
				<fieldset>
					<legend class="screen_out">로그인 정보 입력폼</legend>
					<div class="box_login">
						<div class="inp_text">
							<label for="loginId" class="screen_out">아이디</label>
							<input type="email" id="loginId" name="loginId" placeholder="ID">
						</div>
						<div class="inp_text">
							<label for="loginPw" class="screen_out">비밀번호</label>
							<input type="password" id="loginPw" name="password" placeholder="Password">
						</div>
					</div>
					<button type="submit" class="btn_login" disabled="disabled">로그인</button>
					<div class="login_append">
						<div class="inp_chk"> <!-- 체크시 checked 추가 -->
							<input type="checkbox" id="keepLogin" class="inp_radio" name="keepLogin"><label for="keepLogin" class="lab_g"><span class="img_top ico_check"></span><span class="txt_lab">로그인 상태 유지</span></label>
						</div>
						<span class="txt_find">
				 			<a href="/member/find/loginId" class="link_find">아이디</a>
				 			 / 
				 			<a href="/member/find/password" class="link_find">비밀번호 찾기</a>
				 		</span>
					</div>
					
				</fieldset>
			<input type="hidden" name="fp" value="aeb094adb52ea7584acf361532bcadf7"></form>
		</div>
	</div>
</div>
					</div>
				</div>
			</div>
			<hr class="hide">
		</div>
		<script src="//t1.daumcdn.net/tistory_admin/assets/tistory-web-top/1574742493/static/js/T.js"></script>
		<script src="//t1.daumcdn.net/tistory_admin/assets/tistory-web-top/1574742493/static/js/T.util.js"></script>
		<script src="//t1.daumcdn.net/tistory_admin/assets/tistory-web-top/1574742493/static/js/T.auth.js"></script>
		<script src="//t1.daumcdn.net/tistory_admin/assets/tistory-web-top/1574742493/static/js/pc/T.p.top.js"></script>
		<script src="//t1.daumcdn.net/tistory_admin/assets/tistory-web-top/1574742493/static/js/pc/T.p.top.auth.js"></script>
	

</body></html>
'''

from bs4 import BeautifulSoup


def parse(pageString):
    bsobj = BeautifulSoup(pageString, "html.parser")
    title = bsobj.find("title")
    print(title)
    print(title.text)
    print("-------- parsing --------")
    bu1 = bsobj.find("button", {"class":"btn_login"})
    print(bu1)
    print(bu1.text)

parse(pageString)

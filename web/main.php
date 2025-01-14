<?php include  $_SERVER['DOCUMENT_ROOT']."/db.php"; ?>
<!doctype html>
<head>
<meta charset="UTF-8">
<title>중고플랫폼 통합 서비스</title>
<link rel="stylesheet" type="text/css" href="css/style.css" />
</head>
<body>
  <div id="main_area"> 
    <div style="padding-top:100px; width:parent; height:120px; margin:auto; text-align: center ">
      <h1>중고거래 플랫폼 통합 검색 / 시세 조회 서비스 </h1>
      
    </div>
<div style=" width:parent; height:120px; margin:auto; text-align: center ">
  <div id="search_box">
      <form action="search_result.php" method="get">
      <input type="text" placeholder="검색어 입력" name="search" size="50" required="required"/> <button>검색</button>
    </form>
  </div>
  <h4 style="color:gray; margin-top: 30px; height:10px; ">상품명을 자세히 입력할수록 더 정확한 시세를 확인할 수 있습니다.</h4>
</div>
</div>

<div style="text-align : center; height: 30px; width:30%  margin-top:50px">

     <img width: 100%; height:100%; src="http://www.todayeconomic.com/data/photos/20210312/art_16167464844597_9b1b24.png">

</div>

</body>
</html>
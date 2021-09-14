//알림 권한 요청
function getNotificationPermission(){
    //브라우저 체크
    if(!("Notification" in window)){
        alert("알림 기능을 지원하지 않는 브라우저입니다. 크롬/엣지 등의 최신 브라우저를 사용해주십시오.");
    }
    //이미 동의시
    else if (Notification.permission=="granted"){
        var notification=new Notification("hello");
    }
    //만약 기본 상태일시
    else if (Notification.permission!="denied"){
        Notification.requestPermission().then(function (permission){
            if (permission=="granted"){
                var notification=new Notification("hello");
            }
        });
    }
    //이미 거부시 아무것도 뜨지 않도록
}

window.onload=getNotificationPermission();
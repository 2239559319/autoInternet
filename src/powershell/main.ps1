Add-Type -AssemblyName System.Net.Http

function getLogMsg () {         #获取登录字符串
    $url = "http://192.168.2.135"
    $client = New-Object System.Net.Http.HttpClient
    $response = $client.GetAsync($url)
    $text = $response.Result.Content.ReadAsStringAsync().Result
    
    try {
        if($text -match "href='(\S+)'"){
            $href = $Matches[1]
            return $href.Split("?")[1]
        }
        else {
            Write-Host "已登录"
        }
    }
    catch {
        Write-Host "已登录"
    }
}

#登录
function login {
    param (
        [string]$userId,
        [string]$password
    )
    
}
#获取下线信息
function getLogoutMsg () {
    $client = New-Object System.Net.Http.HttpClient
    $response = $client.GetAsync("http://192.168.2.135/eportal/InterFace.do?method=getOnlineUserInfo")
    $text = $response.Result.Content.ReadAsStringAsync().Result
    $jsonmsg = ConvertFrom-Json -InputObject $text
    return $jsonmsg.userIndex
}

function logout () {
    $userIndex = getLogoutMsg
    $keyValues=New-Object 'System.Collections.Generic.Dictionary[[string],[string]]'
    $keyValues.Add("userIndex",$userIndex)
    $data=New-Object System.Net.Http.FormUrlEncodedContent($keyValues)

    $client = New-Object System.Net.Http.HttpClient
    $response = $client.PostAsync("http://192.168.2.135/eportal/InterFace.do?method=logout",$data)
    $text = $response.Result.Content.ReadAsStringAsync().Result
    $jsonmsg = ConvertFrom-Json -InputObject $text
    <#
    if($jsonmsg["message"].Equals("下线成功！")){
        Write-Host "下线成功"
    }
    else {
        Write-Host "已下线"
    }
    #>
}
logout
function Tg-SendMessage {
    param (
        $Data = "Hello PowerShell",
        $TokenID = "Your_tg_token",
        $ChatID = "Your_chat_ID"
    )

    $url = "https://api.telegram.org/bot$TokenID/sendMessage"

    $payload = @{
        chat_id = $ChatID
        text = $Data
        parse_mode = 'html'
        disable_notification = $false
    }

    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12

    try {
        $response = Invoke-RestMethod -Uri $url -Method Post -ContentType "application/json;charset=utf-8" -Body (ConvertTo-Json -Compress -InputObject $payload)
        if ($response.ok) {
            Write-Host "Your message sent!"
        } else {
            Write-Host "Something happened: $($response.error_code) - $($response.description)"
        }
    }
    catch {
        Write-Host "Error send message: $_"
    }
}

Tg-SendMessage

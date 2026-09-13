# Memperbarui seluruh field (Daftar Isi, Daftar Gambar/Tabel/Kode, nomor
# keterangan) pada Buku-Ajar-PBO.docx melalui Microsoft Word, menyimpan
# ulang berkas, lalu mengekspor PDF pratinjau ke keluaran/ memakai
# LibreOffice (ekspor PDF bawaan Word dapat macet saat berjalan tanpa jendela).
#
# Pemakaian (dari folder buku-ajar-pbo):
#   python tools/build_docx.py
#   powershell -ExecutionPolicy Bypass -File tools/pratinjau.ps1

$akar = Split-Path -Parent $PSScriptRoot
$docx = Join-Path $akar "Buku-Ajar-PBO.docx"
$folderPdf = Join-Path $akar "keluaran"
$soffice = "C:\Program Files\LibreOffice\program\soffice.exe"
New-Item -ItemType Directory -Force $folderPdf | Out-Null

function Repaginate-Aman($doc) {
    try { $doc.Repaginate() }
    catch { Write-Output "peringatan: Repaginate() gagal ($($_.Exception.Message)), lanjut tanpa itu" }
}

$word = New-Object -ComObject Word.Application
$word.Visible = $true
$word.DisplayAlerts = 0
try {
    $doc = $word.Documents.Open($docx)
    $doc.Fields.Update() | Out-Null
    Repaginate-Aman $doc
    foreach ($daftar in $doc.TablesOfContents) { $daftar.Update() }
    Repaginate-Aman $doc
    foreach ($daftar in $doc.TablesOfContents) { $daftar.UpdatePageNumbers() }
    $halaman = $doc.ComputeStatistics(2)  # 2 = wdStatisticPages
    $doc.Save()
    $doc.Close()
    Write-Output "field diperbarui: $docx ($halaman halaman menurut Word)"
}
finally {
    $word.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
}

if (Test-Path $soffice) {
    $p = Start-Process -FilePath $soffice -Wait -PassThru -NoNewWindow `
        -ArgumentList '--headless', '--convert-to', 'pdf', '--outdir', "`"$folderPdf`"", "`"$docx`""
    Write-Output "PDF pratinjau   : $(Join-Path $folderPdf 'Buku-Ajar-PBO.pdf') (kode keluar $($p.ExitCode))"
}
else {
    Write-Output "LibreOffice tidak ditemukan; PDF pratinjau dilewati."
}

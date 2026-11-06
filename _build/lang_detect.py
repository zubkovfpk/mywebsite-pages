RU_TZ = r'^(Europe\/(Moscow|Kaliningrad|Samara|Volgograd|Kirov|Astrakhan|Saratov|Ulyanovsk|Minsk)|Asia\/(Yekaterinburg|Omsk|Novosibirsk|Barnaul|Tomsk|Novokuznetsk|Krasnoyarsk|Irkutsk|Chita|Yakutsk|Khandyga|Vladivostok|Ust-Nera|Magadan|Sakhalin|Srednekolymsk|Kamchatka|Anadyr))$'
def lang_script(cur, alt):
    return ('<script>(function(){try{'
        "var ua=navigator.userAgent;if(/bot|crawl|spider|slurp|lighthouse|preview/i.test(ua))return;"
        "if(sessionStorage.getItem('lang-checked'))return;sessionStorage.setItem('lang-checked','1');"
        "var want=localStorage.getItem('site-lang');"
        "if(!want){var l=(navigator.languages||[navigator.language||'']).join(',').toLowerCase(),tz='';"
        "try{tz=Intl.DateTimeFormat().resolvedOptions().timeZone||''}catch(e){}"
        "want=(/(^|,)(ru|be)(-|,|$)/.test(l)||/" + RU_TZ + "/.test(tz))?'ru':'en';}"
        f"if(want!=='{cur}')location.replace('{alt}'+location.hash);"
        '}catch(e){}})();</script>')

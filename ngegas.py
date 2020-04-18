import tweepy
import time
import anyar
import consent

def ngentot():

    auth = tweepy.OAuthHandler(consent.API_KEY, consent.API_KEY_TOKEN)
    auth.set_access_token(consent.ACCESS_TOKEN, consent.ACCESS_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

    try :
        api.verify_credentials()
        print('otentikasi berhasil')
    except Exception as e:
        print(e)
    apdet = ('WOY ', anyar.nama_orang.upper(), ' BALIKIN DUIT GW ', anyar.gaspol, ', LO KEMARIN PINJEM ', anyar.uwang.upper(), ' BUAT BAYARIN MAKAN SAMA ', anyar.nama_pinjam.upper())
    setring = ''.join(apdet)

    print('Updating Statuses.....')
    print(setring)
    update_status = api.update_status(status= setring)
    update_status

if __name__ == "__main__":
    ngentot()
    time.sleep(60*60)

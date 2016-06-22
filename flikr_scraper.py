from flickr_api.api import flickr
import flickr_api
import authentication

import csv

import time



api_key, secret=authentication.get_keys()

flickr_api.set_keys(api_key = api_key, api_secret = secret)

ApolloArchive=flickr_api.Person.findByUserName("Apollo Image Gallery")



t0 = time.time()

#There are 143 pages if we have 100 photos per page

subjid=401
csv_outfile="ApolloImages_MetaFile.csv"

with open(csv_outfile, "wb"):
    writer = csv.writer(open(csv_outfile, "wb"), delimiter=',')
for i in range(4, 20):
    photos=ApolloArchive.getPublicPhotos(page=i, per_page=100)

    for p in photos:

        


        flickr_id=p.getInfo()["owner"]["id"]
        Attribution=p.getInfo()["owner"]["username"]
        p_id=p.getInfo()["id"]
        date_taken=p.getInfo()["taken"]
        description=p.getInfo()["description"]

        url="https://www.flickr.com/photos/{}/{}".format(flickr_id, p_id)
        filename="{}.jpg".format(p_id)
        savepath="ApolloPhotos/{}".format(filename)

        print "Saving Photo {} as {}".format(subjid, filename)

        p.save(savepath, size_label = 'Medium 640')
        writer.writerow( (subjid, filename, url, description, date_taken))
        

        subjid+=1


print "\n\nTime taken: {}\n\n".format(time.time()-t0)
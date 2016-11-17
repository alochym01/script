import facebook

graph = facebook.GraphAPI(access_token='CAAKZB8aoNPK8BAJSLrjhCQbLEs4dH8SxbJIcYZCjOr4zBEl0wR1PZCyf3RAcU3w00ZAPn5tz538dJ4cGb9Qiy7tmMHEHJC1bZAlXehsGLLiXgbmcA0SNDOvP2SIcS7yPVleGQUn1ZAfQPwc1ZBFSSefLpkZCZCy2j5NaDXah3NEUn2Sj1YqartFEc3SRXcypPdrIZD')

photo = graph.put_photo(image=open('/home/hadn/Downloads/infonet_ca_chet_2.jpg', 'rb'),
                                                    message='Look at this cool photo!',)

# get all links facebook cdn
photoid = '%s?fields=images' % photo['id']
img_links = graph.get_object(id=photoid)
print img_links

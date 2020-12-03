from .. import Provider as AddressProvider


class Provider(AddressProvider):

    city_formats = ('{{city_name}}', )

    street_name_formats = (
        '{{first_name}} {{last_name}}',
        '{{last_name}}',
    )

    street_address_formats = ('{{building_number}} {{street_name}}', )

    address_formats = ('{{street_address}}\n{{city}} {{postcode}}',
                       '{{street_address}}\n{{city}}-{{postcode}}')

    building_number_formats = (
        '####', '###', '##', '#', '#/#', '##/##', '##/###', '##/####')

    postcode_formats = ('######', )

    cities = (
        'आदिलाबाद',
        'अगरतला',
        'अहमदाबाद',
        'अहमदनगर',
        'अजमेर',
        'अम्बाजी',
        'अमरपुर',
        'इलाहाबाद',
        'अकोला',
        'अखनूर',
        'अन्तर्गत',
        'अलांग',
        'अलीगढ',
        'दादरा और नगर हवेली',
        'अमरावती',
        'अमरोहा',
        'अनन्तपुर',
        'करना',
        'जिससेबेलारी',
        'अनंतनाग',
        'भागलपुर',
        'भद्रक',
        'बचेली',
        'बहादुरगंज',
        'बहादुरगढ',
        'चिरमिरी',
        'चिराला',
        'चित्रदुर्ग',
        'चित्तूर',
        'चित्रकूट',
        'देवगढ़',
        'दालखोला',
        'देवास',
        'चंडीगढ',
        'चिपलुन',
        'चक्रधरपुर',
        'चंबा',
        'फतहपुर',
        'फतेहपुर',
        'फतेहगढ',
        'सभापतिने',
        'देवगढ़',
        'धर्मापुरी',
        'पाकाला',
        'धारवाड',
        'असम',
        'देहरा',
        'रानीताल',
        'खडगपुर',
        'मोकामा',
        'मोकोकचुंग',
        'जिलोंपर',
        'विस्तारण',
        'मोतिहारी',
        'लखनऊ',
        'मुंबई',
        'हैदराबाद',
    )

    states = (
        'अरूणाचल प्रदेश',
        'बिहार',
        'असम',
        'आंध्र प्रदेश',
        'छत्तीसगढ',
        'हरियाणा',
        'गुजरात',
        'हिमाचल प्रदेश',
        'गोवा',
        'मध्य प्रदेश',
        'महाराष्ट्र',
        'जम्मू और कश्मीर',
        'केरल',
        'कर्नाटक',
        'मणिपुर',
        'मिजोरम',
        'मेघालय',
        'सिक्किम',
        'राजस्थान',
        'पंजाब',
        'उडीसा',
        'उत्तरांचल',
        'उत्तर प्रदेश',
        'तमिलनाडु',
        'त्रिपुरा',
        'पश्चिमी बंगाल',
        'अंडमान और निकोबार',
        'दमन और दीव',
        'दादरा और नगर हवेली',
        'दिल्ली',
        'पांडिचेरी',
        'लक्षद्वीप',
    )

    countries = (
        'आर्मीनिया',
        'यू.के.',
        'फ्रांस',
        'फलस्तीन',
        'मिस्र',
        'ब्राज़ील',
        'ईरान',
        'यूनान',
        'स्पेन',
        'जॉर्जिया',
        'लेबनान',
        'सायप्रस',
        'सीरिया',
        'कनाडा',
        'रूस',
        'संयुक्त राज्य अमरीका',
        'नेदर्लान्ड',
        'ऑस्ट्रेलिया',
        'एंटीगुआ',
        'बार्बुडा',
        'ऑस्ट्रिया',
        'अज़रबाइजान',
        'बारबाडोस',
        'बेलारूस',
        'बेल्जियम',
        'बेलीज़',
        'बेनिन',
        'बहामास',
        'बहरीन',
        'बांग्लादेश',
        'भूटान',
        'बोलिविया',
        'बोस्निया',
        'हर्जेगोविना',
        'बोत्सवाना',
        'ब्रुनेई',
        'बुल्गारिया',
        'बुर्किना फ़ासो',
        'बर्मा',
        'बुरूंडी',
        'डोमिनिकन रिपब्लिक',
        'गिनिया',
        'टीमोर',
        'फ़िनलैंड',
        'गेबोन',
        'गाम्बिया',
        'जर्मनी',
        'ग्रेनेडा',
        'घाना',
        'ग्रेट ब्रिटेन',
        'हंगरी',
        'भारत',
        'हिन्दुस्तान',
        'इराक',
        'आयरलैंड',
        'इंडोनेशिया',
        'इटली',
        'जमैका',
        'जॉर्डन',
        'जापान',
        'क़जाख़स्तान',
        'केन्या',
        'किरिबाती',
        'दक्षिण कोरिया',
        'लातविया',
        'लाओस',
        'उत्तर कोरिया',
        'कोसोवो',
        'कुवैत',
        'लेबनान',
        'लिचटीनस्टीन',
        'लिथुआनिया',
        'लक्समबर्ग',
        'लीबिया',
        'लाइबेरिया',
        'लेसोथो',
        'नेपाल',
        'न्यूज़ीलैण्ड',
        'निकारागुआ',
        'नाइजर',
        'नाउरू',
        'सेंट लुसिया',
        'रोमानिया',
        'अरब अमीरात',
        'यूएई',
        'युगांडा',
        'यूक्रेन',
        'उरूग्वे',
        'उज़बेकिस्तान',
        'यूनाइटेड किंगडम',
        'वानुआतू',
        'वेटिकन सिटी',
        'वेनेजुएला',
        'पश्चिमी सहारा',
        'वियतनाम',
        'यमन',
        'ज़ायर',
        'ज़ाम्बिया',
        'ज़िम्बाब्वे',
        'पाकिस्तान',
        'सउदी अरब',
        'ओमान',
        'क़तर',
        'ट्यूनीशिया',
        'मोरक्को',
        'तुर्की',
        'श्रीलंका',
        'अफ़ग़ानिस्तान',
    )

    def city_name(self):
        return self.random_element(self.cities)

    def state(self):
        return self.random_element(self.states)

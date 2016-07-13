<?php

class Curl
{

    public $cookieFile = 'cookie.txt';

    public $cookieKey = '';

    public $cookieName = '';

    public $headers = array();

    public $options = array();

    public $httpHeader = array(
        'Accept: application/json, text/javascript, */*; q=0.01',
        'Cache-Control: max-age=0',
        "Content-type: application/x-www-form-urlencoded; charset=UTF-8",
        'Connection: keep-alive',
        'X-Requested-With: XMLHttpRequest',
        'Keep-Alive: 300'
    );

    public $encoding = 'gzip,deflate,sdch';

    public $referer = 'http://hdonline.vn';

    public $user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36';

    // public $_interface = '85.17.65.44';

    protected $error = '';

    protected $handle;

    public function setHeaderXMLHttpRequest() {
        curl_setopt($this->handle, CURLOPT_HTTPHEADER, array('X-Requested-With: XMLHttpRequest'));
    }

    /**
     * Contructor
     * @param string $htaccessUsername
     * @param string $htaccessPassword
     * @author Hieu Le
     */
    public function __construct ()
    {

        $this->handle = curl_init();

        // Set some default CURL options
        curl_setopt($this->handle, CURLOPT_COOKIEFILE, $this->cookieFile);
        curl_setopt($this->handle, CURLOPT_COOKIEJAR, $this->cookieFile);
        curl_setopt($this->handle, CURLOPT_COOKIESESSION, true);
        if ($this->cookieKey != "") {
            curl_setopt($this->handle, CURLOPT_COOKIE,
                $this->cookieKey . '=' . $this->cookieName . '; path=/');
        }
        curl_setopt($this->handle, CURLOPT_HTTPHEADER, $this->httpHeader);
        curl_setopt($this->handle, CURLOPT_ENCODING, $this->encoding);
        curl_setopt($this->handle, CURLOPT_FOLLOWLOCATION, true);
        curl_setopt($this->handle, CURLOPT_HEADER, false);
        curl_setopt($this->handle, CURLOPT_REFERER, $this->referer);

        // TRUE to automatically set the Referer
        curl_setopt($this->handle, CURLOPT_AUTOREFERER, TRUE);

        curl_setopt($this->handle, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($this->handle, CURLOPT_USERAGENT, $this->user_agent);
        // curl_setopt($this->handle, CURLOPT_INTERFACE, '85.17.65.44');

        if (isset($this->_interface) && $this->_interface != false) {
            curl_setopt($this->handle, CURLOPT_INTERFACE, $this->_interface);
        }

//         if ($auth_user || $auth_pass)
//         {
//             curl_setopt($this->handle, CURLOPT_USERPWD, "{$auth_user}:{$auth_pass}");
//             curl_setopt($this->handle, CURLOPT_HTTPAUTH, CURLAUTH_ANY);
//         }

        /**
         * My CUSTOM HEADER CALLBACK
         */
        curl_setopt($this->handle, CURLOPT_HEADERFUNCTION,
            "\Curl::curlHeaders");

        // Format custom headers for this request and set CURL option
        $headers = array();
        foreach ($this->headers as $key => $value) {
            $headers[] = $key . ': ' . $value;
        }
//        curl_setopt($this->handle, CURLOPT_HTTPHEADER, $headers);

        // Set any custom CURL options
        foreach ($this->options as $option => $value) {
            curl_setopt($this->handle,
                constant(
                    'CURLOPT_' . str_replace('CURLOPT_', '',
                        strtoupper($option))), $value);
        }
    }

    public function unsetCookie ()
    {
        if (file_exists($this->cookieFile)) {
            unlink($this->cookieFile);
        }
    }

    public function delete ($url, $vars = array())
    {
        return $this->request('DELETE', $url, $vars);
    }

    public function error ()
    {
        return $this->error;
    }

    public function get ($url, $vars = array())
    {
        if (! empty($vars)) {
            $url .= (stripos($url, '?') !== false) ? '&' : '?';
            $url .= http_build_query($vars, '', '&');
        }
        return $this->request('GET', $url);
    }

    public function post ($url, $vars = array())
    {
        return $this->request('POST', $url, $vars);
    }

    public function put ($url, $vars = array())
    {
        return $this->request('PUT', $url, $vars);
    }

    protected function request ($method, $url, $vars = array())
    {
        curl_setopt($this->handle, CURLOPT_POSTFIELDS,
            (is_array($vars) ? http_build_query($vars, '', '&') : $vars));
        // Determine the request method and set the correct CURL option
        switch ($method) {
            case 'GET':
                curl_setopt($this->handle, CURLOPT_HTTPGET, true);
                break;
            case 'POST':
                curl_setopt($this->handle, CURLOPT_POST, true);
                break;
            default:
                curl_setopt($this->handle, CURLOPT_CUSTOMREQUEST, $method);
        }

        curl_setopt($this->handle, CURLOPT_URL, $url);

        $response = curl_exec($this->handle);
        if (! $response) {
            $this->error = curl_errno($this->handle) . ' - ' .
                curl_error($this->handle);
        }
        // curl_close($this->handle);
        return $response;
    }

    /**
     * Close the curl resource
     */
    public function close ()
    {
        if ($this->handle) {
            curl_close($this->handle);
        }
    }

    /**
     * Set the ip/interface for downloading
     */
    public function setInterface ($interface)
    {
        $this->_interface = $interface;
    }

    /**
     * Curl Header function use for debugging
     *
     * @param
     *            curl resource $ch
     * @param string $header
     * @return int
     */
    public static function curlHeaders ($ch, $header)
    {
        if ($ch) {
            // echo $header;
            return strlen($header);
        } else {
            echo "curl not initialized\n";
            return false;
        }
    }
}
?>
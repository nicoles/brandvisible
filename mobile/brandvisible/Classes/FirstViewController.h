//
//  FirstViewController.h
//  brandvisible
//
//  Created by Nicole Aptekar on 10/11/25.
//  Copyright 2010 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>


@interface FirstViewController : UIViewController {
	IBOutlet UILabel *label;
	NSMutableData *responseData;
}

@property (nonatomic, retain) IBOutlet UILabel *label;

@end

var form = FormApp.getActiveForm();

function myFunction() {
  // create an array of images from a google drive folder
  // you'll need the id of the folder
  var imageFolderId = "1kBtdl0ywwlj6vi3cUQO1I2IHacFiX5Qo";
  var imageFolder = DriveApp.getFolderById(imageFolderId);
  var imageFiles = imageFolder.getFiles();
  var imageArray = [];

  while (imageFiles.hasNext()) {
    var image = imageFiles.next();
    var imageName = image.getName()
    imageArray.push([image,imageName]);
  }

  var form = FormApp.getActiveForm();
 
  form.setTitle('ArabIcMemesHateDet')
    .setDescription('In this form, you have to classify the meme picture as either hate speech, only offensive or only humor')
    .setConfirmationMessage('Thanks for classifing!')
    .setAllowResponseEdits(true)
    .setAcceptingResponses(false);

  for(var i=0; i< imageArray.length ;i++) {

    var img = imageArray[i];
    form.addImageItem()
      .setTitle(img[1])
      .setHelpText('Classify Image To Continue') // The help text is the image description
      .setImage(img[0]);
    
    var item7 = form.addMultipleChoiceItem();
    item7.setChoices([ 
          item7.createChoice(img[1], isCorrect=true)
        ]);
        
    item7.setHelpText('Keep this choice selected, if it is not selected please select it.');


    
    var item = form.addMultipleChoiceItem();
        item.setTitle('Image Classified as:('+img[1]+')');

    var item5 = form.addMultipleChoiceItem();
        item5.setTitle('if you want to exit the form please read the description carefully,')
        item5.setHelpText(' Note: if you want to exit the form and separate auditing time you can click (Exit form) , you can re-audit the form by the email you have received. \n if you want to complete the form now, please ignore this button.')
      
    var page2 = form.addPageBreakItem()
                      .setTitle('');
    form.addImageItem()
        .setTitle(img[1])
        .setHelpText('Classify Image To Continue') // The help text is the image description
        .setImage(img[0]);


  
    var item2 = form.addCheckboxItem();
      item2.setTitle('Type of Hate Speech:')
      .setChoices([
        item2.createChoice('Race العرق'),
        item2.createChoice('Religion دين'),
        item2.createChoice('Gender الجنس'),
        item2.createChoice('National origin اصل وطني'),
        item2.createChoice('Disorder, Disability, and Difference (DDD) الاضطراب والاعاقة والاختلاف')
      ])
      .showOtherOption(false);
  



    var item6 = form.addMultipleChoiceItem();
        item6.setTitle('if you want to exit the form please read the description carefully,')
        item6.setHelpText(' Note: if you want to exit the form and separate auditing time you can click (Exit form) , you can re-audit the form by the email you have received. \n if you want to complete the form now, please ignore this button.')
      item6.setChoices([ 
          item6.createChoice('Exit Form',FormApp.PageNavigationType.SUBMIT),
        
        ])
        .showOtherOption(false);

    var page3 = form.addPageBreakItem()
                      .setTitle('');

    item.setChoices([
          item.createChoice('Hate Speech الكلام الذي يحض على الكراهية',page2),
          item.createChoice('Only offensive اساءة فقط',page3),
          item.createChoice('Only humor فكاهة فقط',page3)
        ])
        .showOtherOption(false);

    item5.setChoices([ 
          item5.createChoice('Exit Form',FormApp.PageNavigationType.SUBMIT),
        
        ])
        .showOtherOption(false);
   
  }
}
